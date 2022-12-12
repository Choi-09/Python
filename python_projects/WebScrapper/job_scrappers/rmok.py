from bs4 import BeautifulSoup
import requests


def extract_jobs(keyword):
    url = f"https://remoteok.com/remote-{keyword}-jobs"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})

    results = []
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        jobs = soup.find_all("tr", class_="job")
        # print(jobs)

        for post in jobs:
            job_title = post.find('h2', itemprop="title")
            # print(job_title)

            job_link = post.find("a")["href"]
            # print(job_link)

            company = post.find("h3", itemprop="name")
            # print(company)

            location = post.find_all('div', class_='location tooltip')[:-1]

            for i in location:
                location = i.text
            # print(location)

            job_data = {
                'position': job_title.string.strip(),
                'company': company.string.strip(),
                'location': location,
                'link': f"https://remoteok.com/{job_link}"
            }
            results.append(job_data)
    else:
        print("Can't get jobs.")
    return results
