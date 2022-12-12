from bs4 import BeautifulSoup
import requests


def extract_wwr_jobs(keyword):
    url = f"https://weworkremotely.com/remote-jobs/search?term={keyword}"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})

    results = []
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        jobs = soup.find_all("section", class_="jobs")
        print(jobs)

        for job_section in jobs:
            job_posts = job_section.find_all("li")
            job_posts.pop(-1)

            for post in job_posts:
                anchors = post.find_all('a')
                anchor = anchors[1]
                # print(anchor)
                link = anchor['href']
                company = anchor.find('span', class_="company")
                position = anchor.find('span', class_="title")
                location = anchor.find('span', class_="region company")

                job_data = {
                    'position': position.string.strip(),
                    'company': company.string.strip(),
                    'location': location.string.strip(),
                    'link': f"https://weworkremotely.com{link}"
                }
                results.append(job_data)

    else:
        print("Can't request website")
    return results
