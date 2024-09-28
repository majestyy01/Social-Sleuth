import requests

"""
WoxicDEV - 2024 
SocialSleuth - 2024
Instagram - mertt.js_
LinkedIn : Mert Ali Kaya
chiefdelphi : mrtalikyaa
medium : mrtalikyaa
////////////////////////////////////
YANILMA PAYI OLABİLİR!!
82. satırdaki bölüme ekleme yapıp yanılma payını azaltabilirsiniz.
Yorum satırlarıyla kendinize göre özelleştirebilmeniz için olabildiğince bilgi vermeye çalıştım.
"""
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'

# Kontrol edilecek platformlar isterseniz ekleme yapabilirsiniz ben ssl sorunu vb yaşadığımdan bazılarını kaldırdım
sosyal_medya_platformlari = {
    "Twitter": "https://twitter.com/{}",
    "Instagram": "https://www.instagram.com/{}",
    "GitHub": "https://github.com/{}",
    "Facebook": "https://www.facebook.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "LinkedIn": "https://www.linkedin.com/in/{}",
    "YouTube": "https://www.youtube.com/{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "Pinterest": "https://www.pinterest.com/{}",
    "Snapchat": "https://www.snapchat.com/add/{}",
    "Medium": "https://medium.com/@{}",
    "Flickr": "https://www.flickr.com/people/{}",
    "SoundCloud": "https://soundcloud.com/{}",
    "Vimeo": "https://vimeo.com/{}",
    "DeviantArt": "https://www.deviantart.com/{}",
    "Twitch": "https://www.twitch.tv/{}",
    "Discord": "https://discord.com/users/{}",
    "Dribbble": "https://dribbble.com/{}",
    "Steam": "https://steamcommunity.com/id/{}",
    "Patreon": "https://www.patreon.com/{}",
    "Behance": "https://www.behance.net/{}",
    "Goodreads": "https://www.goodreads.com/user/show/{}",
    "Quora": "https://www.quora.com/profile/{}",
    "ProductHunt": "https://www.producthunt.com/@{}",
    "AngelList": "https://angel.co/u/{}",
    "500px": "https://500px.com/{}",
    "Kickstarter": "https://www.kickstarter.com/profile/{}",
    "GitLab": "https://gitlab.com/{}",
    "Bitbucket": "https://bitbucket.org/{}/",
    "Gravatar": "https://en.gravatar.com/{}",
    "VK": "https://vk.com/{}",
    "Weibo": "https://weibo.com/{}/",
    "Douban": "https://www.douban.com/people/{}",
    "Xing": "https://www.xing.com/profile/{}",
    "Sina Weibo": "https://weibo.com/{}/",
    "MyAnimeList": "https://myanimelist.net/profile/{}",
    "Bandcamp": "https://bandcamp.com/{}",
    "ReverbNation": "https://www.reverbnation.com/{}",
    "Imgur": "https://imgur.com/user/{}",
    "Last.fm": "https://www.last.fm/user/{}",
    "Couchsurfing": "https://www.couchsurfing.com/people/{}",
    "TripAdvisor": "https://www.tripadvisor.com/members/{}",
    "Meetup": "https://www.meetup.com/members/{}",
    "Keybase": "https://keybase.io/{}",
    "Dev.to": "https://dev.to/{}",
    "Foursquare": "https://foursquare.com/{}",
}

def kullanici_kontrol(username):
    print(f"Kullanıcı adın kontrol ediliyor: {username}")
    
    
    dosya_adi = f"{username}.txt"
    # Sonuçları kaydetmek için dosya açma
    with open(dosya_adi, 'w') as f:
        for platform, url in sosyal_medya_platformlari.items():
            full_url = url.format(username)
            response = requests.get(full_url)
            
            if response.status_code == 200:
                if "bu sayfa mevcut değil" in response.text.lower() or "not found" in response.text.lower(): #sayfada bu metin varsa bulunamadı yazıyor bunu çoğaltabilirsiniz.
                    print(f"{YELLOW}[X]bulunamadı(sayfa mevcut değil): {platform}")
                    (f"{username} bulunamadı (sayfa mevcut değil): {platform}\n")#isterseniz txtye kaydedebilirsiniz başına (f.write  yazarak)
                else:
                    print(f"{GREEN}[+] bulundu: {platform} -> {full_url}")
                    f.write(f"{username} bulundu: {platform} -> {full_url}\n")
            else:
                print(f"{RED}[-] bulunamadı: {platform}")
                (f"{username} bulunamadı: {platform}\n") #isterseniz txtye kaydedebilirsiniz başına (f.write  yazarak)

if __name__ == "__main__":
    print(f"{BLUE}   _________             .__       .__    _________.__                 __  .__     ")
    print(f"{BLUE}  /   _____/ ____   ____ |__|____  |  |  /   _____/|  |   ____  __ ___/  |_|  |__        .-.      _______")
    print(f"{BLUE}  \_____  \ /  _ \_/ ___\|  \__  \ |  |  \_____  \ |  | _/ __ \|  |  \   __\  |  \      ()``; |==|_______D") 
    print(f"{BLUE}  /        (  <_> )  \___|  |/ __ \|  |__/        \|  |_\  ___/|  |  /|  | |   Y  \     / ('        /|\   ")
    print(f"{BLUE} /_______  /\____/ \___  >__(____  /____/_______  /|____/\___  >____/ |__| |___|  / (  /  |        / | \  ")
    print(f"{BLUE}         \/            \/        \/             \/           \/                 \/   \(_)_]]      /  |  \  ")
    print(f"{BLUE}                                                                                      -by WoxicDEV           \n\n")
    k_adi = input("Kontrol edilecek kullanıcı adını Giriniz: ")
    kullanici_kontrol(k_adi)
