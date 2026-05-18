from library import download_video, read_video_urls
import time
import ssl
import certifi
import os
from multiprocessing import Pool


ssl._create_default_https_context = ssl._create_unverified_context
os.environ['SSL_CERT_FILE'] = certifi.where()

def main():

    urls = read_video_urls("../data/video_urls.csv")

    total_start = time.perf_counter()
    for url in urls:
        print(f"Starting download: {url}")
        download_video(url)

    total_end = time.perf_counter()
    serial_time = round(total_end - total_start, 2)

    print(f"Serial execution: {serial_time}")
    
    with open("../reports/sequential_report.md", "a") as f:
        f.write(f"\nTotal time: {serial_time} seconds\n")



    start_parallel = time.perf_counter()

    with Pool() as pool:
        pool.map(download_video, urls)

    end_parallel = time.perf_counter()
    parallel_time = round(end_parallel - start_parallel, 2)
    
    print(f"Parallel execution: {parallel_time}")

    with open("../reports/sequential_report.md", "a") as f:
        f.write(f"\n## Parallel execution\n\nTotal time: {parallel_time} seconds\n")

if __name__ == "__main__":
    main()



from multiprocessing import Pool
