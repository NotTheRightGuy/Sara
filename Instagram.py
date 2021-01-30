import requests
from bs4 import BeautifulSoup


def fetch_insta_data(user_profile):
    """
    :param user_profile: The username of instagram user in string format
    :return: A dictionary with name, followers and following respectively
    """
    user_profile_website = ("https://www.instagram.com/{}/".format((user_profile.lower())))
    website = requests.get(user_profile_website)
    soup = BeautifulSoup(website.text,'lxml')
    data = soup.find_all('meta', attrs={'property': 'og:description'})
    text = data[0].get('content').split()
    user = '%s %s %s' % (text[-3], text[-2], text[-1])
    followers = text[0]
    following = text[2]
    final_data = {'Name':user,'Followers':followers,'Following':following}
    return final_data

