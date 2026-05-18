from library import download_video, read_video_urls, get_video_metadata
import time
import ssl
import certifi
import os
import csv
from multiprocessing import Pool


ssl._create_default_https_context = ssl._create_unverified_context
os.environ['SSL_CERT_FILE'] = certifi.where()

def main():

    urls = read_video_urls("../data/video_urls.csv")

    metadata_rows = []
    for url in urls:
        data = get_video_metadata(url)
        metadata_rows.append(data)

    with open("data/video_metadata.csv", "w", newline="") as file:
        fieldnames = ["title", "duration", "uploader", "view_count", "ext", "url"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(metadata_rows)


    # total_start = time.perf_counter()
    # for url in urls:
    #     download_video(url)

    # total_end = time.perf_counter()
    # serial_time = round(total_end - total_start, 2)

    # print(f"Serial execution: {serial_time}")
    
    # with open("../reports/sequential_report.md", "a") as f:
    #     f.write(f"\nTotal time: {serial_time} seconds\n")



    start_parallel = time.perf_counter()

    with Pool() as pool:
        results = pool.map(download_video, urls)

    end_parallel = time.perf_counter()
    parallel_time = round(end_parallel - start_parallel, 2)
    
    successes = 0
    failures = 0

    for result in results:
        if result["status"] == "failed":
            print("Failed:", result["url"])
            print("Error:", result["error"])
            failures += 1
        else:
            successes += 1

    with open("../reports/sequential_report.md", "a") as f:
        f.write(f"\n## Parallel execution\n\nTotal time: {parallel_time} seconds\n")
        f.write(f"Successful downloads: {successes}\n")
        f.write(f"Failed downloads: {failures}\n")

        for result in results:
            if result["status"] == "failed":
                f.write(f"- {result['url']} | Error: {result['error']}\n")

if __name__ == "__main__":
    main()