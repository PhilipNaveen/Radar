#imports
import socket
import sys 
import time 
import requests

#class_[COLORS]
class COLORS:
    RED = '\033[91m'
    BLUE = '\033[96m'
    WHITE = '\033[97m'
    GREEN = '\033[92m'

#def_[banner]
def banner():
    print(COLORS.WHITE + '''
                                    ▓▓▓▓                                                                  
                                  ▓▓    ▓▓                                                                
                                  ▓▓  ░░  ▓▓                    ▓▓▓▓▓▓                                    
                                  ▓▓  ░░░░  ▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ░░▓▓                                  
                                  ▓▓  ░░░░░░  ██              ▓▓  ░░░░▓▓                                  
                                  ▓▓  ░░░░░░░░  ▓▓            ▓▓░░░░░░▓▓                                  
                                  ▓▓  ░░░░░░░░░░  ██          ▓▓▓▓▓▓▓▓                                    
                                    ▓▓  ░░░░░░░░░░  ▓▓      ▓▓      ▓▓                                    
                                    ▓▓  ░░░░░░░░░░░░  ▓▓  ▓▓        ▓▓                                    
                                    ▓▓  ░░░░░░░░░░░░░░  ▓▓          ▓▓                                    
                                      ▓▓  ░░░░░░░░░░░░░░  ▓▓        ▒▒                                    
                                      ▓▓  ░░░░░░░░░░░░░░░░  ▓▓      ▓▓                                    
                                        ▓▓  ░░░░░░░░░░░░░░░░  ▓▓    ▓▓                                    
                                        ▓▓  ░░░░░░░░░░░░░░░░░░  ▓▓  ▓▓                                    
                                        ▓▓▓▓░░░░░░░░░░░░░░░░░░░░  ▓▓                                      
                                        ▓▓░░▓▓░░░░░░░░░░░░░░░░░░░░  ▓▓                                    
                                        ▓▓  ░░▓▓░░░░░░░░░░░░░░░░░░░░  ▓▓                                  
                                      ▓▓  ░░░░░░▓▓▓▓░░░░░░░░░░░░░░░░░░  ▓▓                                
                                      ▓▓  ░░░░░░░░░░▓▓▓▓░░░░░░░░░░░░░░░░  ▓▓                              
                                      ██  ░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░░░░░░▓▓                              
                                    ▓▓  ░░░░░░░░░░░░░░░░▓▓    ▓▓▓▓▓▓▓▓▓▓▓▓                                
                                    ▓▓  ░░░░░░░░░░░░░░░░▓▓                                                
                ░░                  ▓▓  ░░░░░░░░░░░░░░░░▓▓                                                
                                    ▓▓  ░░░░░░░░░░░░░░░░▓▓                                                
                                  ▓▓  ░░░░░░░░░░░░░░░░░░░░▓▓                                              
                                  ▓▓  ░░░░░░░░░░░░░░░░░░░░▓▓                                              
                                  ▒▒  ░░░░░░░░░░░░░░░░░░░░▓▓                                              
                                ▒▒  ░░░░░░░░░░░░░░░░░░░░░░░░▓▓                ░░                          
                                ▓▓  ░░░░░░░░░░░░░░░░░░░░░░░░▓▓                                            
                                ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓                                            
                                ░░▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▒▒▓▓▓▓                                  
    ''')
    print(COLORS.RED + 'use:' + COLORS.BLUE + ' track lost accounts')
    print(COLORS.RED + 'warning:' + COLORS.BLUE + ' no tracking other people')
    print(COLORS.RED + 'made:' + COLORS.BLUE + ' none')
    print(COLORS.RED + 'program name:' + COLORS.BLUE + 'account_finder')
    print(COLORS.RED + 'built with:' + COLORS.BLUE + 'python 3.83')

#class_[hunt_lost_accounts]
class hunt_lost_accounts:
    
    #init_[self//optional_parameters]
    def __init__(self):  
        username = str(input(COLORS.RED + '\nenter the username for searching: '))

        # INSTAGRAM
        instagram = f'https://www.instagram.com/{username}'
        # FACEBOOK
        facebook = f'https://www.facebook.com/{username}'
        #TWITTER
        twitter = f'https://www.twitter.com/{username}'
        # YOUTUBE
        youtube = f'https://www.youtube.com/{username}'
        # BLOGGER
        blogger = f'https://{username}.blogspot.com'
        # GOOGLE+
        google_plus = f'https://plus.google.com/s/{username}/top'
        # REDDIT
        reddit = f'https://www.reddit.com/user/{username}'
        # WORDPRESS
        wordpress = f'https://{username}.wordpress.com'
        # PINTEREST
        pinterest = f'https://www.pinterest.com/{username}'
        # GITHUB
        github = f'https://www.github.com/{username}'
        # TUMBLR
        tumblr = f'https://{username}.tumblr.com'
        # FLICKR
        flickr = f'https://www.flickr.com/people/{username}'
        # STEAM
        steam = f'https://steamcommunity.com/id/{username}'
        # VIMEO
        vimeo = f'https://vimeo.com/{username}'
        # SOUNDCLOUD
        soundcloud = f'https://soundcloud.com/{username}'
        # DISQUS
        disqus = f'https://disqus.com/by/{username}'
        # MEDIUM
        medium = f'https://medium.com/@{username}'
        # DEVIANTART
        deviantart = f'https://{username}.deviantart.com'
        # VK
        vk = f'https://vk.com/{username}'
        # ABOUT.ME
        aboutme = f'https://about.me/{username}'
        # IMGUR
        imgur = f'https://imgur.com/user/{username}'
        # FLIPBOARD
        flipboard = f'https://flipboard.com/@{username}'
        # SLIDESHARE
        slideshare = f'https://slideshare.net/{username}'
        # FOTOLOG
        fotolog = f'https://fotolog.com/{username}'
        # SPOTIFY
        spotify = f'https://open.spotify.com/user/{username}'
        # MIXCLOUD
        mixcloud = f'https://www.mixcloud.com/{username}'
        # SCRIBD
        scribd = f'https://www.scribd.com/{username}'
        # BADOO
        badoo = f'https://www.badoo.com/en/{username}'
        # PATREON
        patreon = f'https://www.patreon.com/{username}'
        # BITBUCKET
        bitbucket = f'https://bitbucket.org/{username}'
        # DAILYMOTION
        dailymotion = f'https://www.dailymotion.com/{username}'
        # ETSY
        etsy = f'https://www.etsy.com/shop/{username}'
        # CASHME
        cashme = f'https://cash.me/{username}'
        # BEHANCE
        behance = f'https://www.behance.net/{username}'
        # GOODREADS
        goodreads = f'https://www.goodreads.com/{username}'
        # INSTRUCTABLES
        instructables = f'https://www.instructables.com/member/{username}'
        # KEYBASE
        keybase = f'https://keybase.io/{username}'
        # KONGREGATE
        kongregate = f'https://kongregate.com/accounts/{username}'
        # LIVEJOURNAL
        livejournal = f'https://{username}.livejournal.com'
        # ANGELLIST
        angellist = f'https://angel.co/{username}'
        # LAST.FM
        last_fm = f'https://last.fm/user/{username}'
        # DRIBBBLE
        dribbble = f'https://dribbble.com/{username}'
        # CODECADEMY
        codecademy = f'https://www.codecademy.com/{username}'
        # GRAVATAR
        gravatar = f'https://en.gravatar.com/{username}'
        # PASTEBIN
        pastebin = f'https://pastebin.com/u/{username}'
        # FOURSQUARE
        foursquare = f'https://foursquare.com/{username}'
        # ROBLOX
        roblox = f'https://www.roblox.com/user.aspx?username={username}'
        # GUMROAD
        gumroad = f'https://www.gumroad.com/{username}'
        # NEWSGROUND
        newsground = f'https://{username}.newgrounds.com'
        # WATTPAD
        wattpad = f'https://www.wattpad.com/user/{username}'
        # CANVA
        canva = f'https://www.canva.com/{username}'
        # CREATIVEMARKET
        creative_market = f'https://creativemarket.com/{username}'
        # TRAKT
        trakt = f'https://www.trakt.tv/users/{username}'
        # 500PX
        five_hundred_px = f'https://500px.com/{username}'
        # BUZZFEED
        buzzfeed = f'https://buzzfeed.com/{username}'
        # TRIPADVISOR
        tripadvisor = f'https://tripadvisor.com/members/{username}'
        # HUBPAGES
        hubpages = f'https://{username}.hubpages.com'
        # CONTENTLY
        contently = f'https://{username}.contently.com'
        # HOUZZ
        houzz = f'https://houzz.com/user/{username}'
        #BLIP.FM
        blipfm = f'https://blip.fm/{username}'
        # WIKIPEDIA
        wikipedia = f'https://www.wikipedia.org/wiki/User:{username}'
        # HACKERNEWS
        hackernews = f'https://news.ycombinator.com/user?id={username}'
        # CODEMENTOR
        codementor = f'https://www.codementor.io/{username}'
        # REVERBNATION
        reverb_nation = f'https://www.reverbnation.com/{username}'
        # DESIGNSPIRATION
        designspiration = f'https://www.designspiration.net/{username}'
        # BANDCAMP
        bandcamp = f'https://www.bandcamp.com/{username}'
        # COLOURLOVERS
        colourlovers = f'https://www.colourlovers.com/love/{username}'
        # IFTTT
        ifttt = f'https://www.ifttt.com/p/{username}'
        # EBAY
        ebay = f'https://www.ebay.com/usr/{username}'
        # SLACK
        slack = f'https://{username}.slack.com'
        # OKCUPID
        okcupid = f'https://www.okcupid.com/profile/{username}'
        # TRIP
        trip = f'https://www.trip.skyscanner.com/user/{username}'
        # ELLO
        ello = f'https://ello.co/{username}'
        # TRACKY
        tracky = f'https://tracky.com/user/~{username}'
        # BASECAMP
        basecamp = f'https://{username}.basecamphq.com/login'

        self.websites = [
            instagram, facebook, twitter, youtube, blogger, google_plus, reddit,
            wordpress, pinterest, github, tumblr, flickr, steam, vimeo, soundcloud, disqus, 
            medium, deviantart, vk, aboutme, imgur, flipboard, slideshare, fotolog, spotify,
            mixcloud, scribd, badoo, patreon, bitbucket, dailymotion, etsy, cashme, behance,
            goodreads, instructables, keybase, kongregate, livejournal, angellist, last_fm,
            dribbble, codecademy, gravatar, pastebin, foursquare, roblox, gumroad, newsground,
            wattpad, canva, creative_market, trakt, five_hundred_px, buzzfeed, tripadvisor, hubpages,
            contently, houzz, blipfm, wikipedia, hackernews, reverb_nation, designspiration,
            bandcamp, colourlovers, ifttt, ebay, slack, okcupid, trip, ello, tracky, basecamp
            ]
        self.website_names_for_socket = [
            'instagram', 'facebook', 'twitter', 'youtube', 'blogger', 'google_plus', 'reddit',
            'wordpress', 'pinterest', 'github', 'tumblr', 'flickr', 'steam', 'vimeo', 'soundcloud', 'disqus', 
            'medium', 'deviantart', 'vk', 'aboutme', 'imgur', 'flipboard', 'slideshare', 'fotolog', 'spotify',
            'mixcloud', 'scribd', 'badoo', 'patreon', 'bitbucket', 'dailymotion', 'etsy', 'cashme', 'behance',
            'goodreads', 'instructables', 'keybase', 'kongregate', 'livejournal', 'angellist', 'last_fm',
            'dribbble', 'codecademy', 'gravatar', 'pastebin', 'foursquare, roblox', 'gumroad', 'newsground',
            'wattpad', 'canva', 'creative_market', 'trakt', 'five_hundred_px, buzzfeed', 'tripadvisor', 'hubpages',
            'contently', 'houzz', 'blipfm', 'wikipedia', 'hackernews', 'reverb_nation', 'designspiration',
            'bandcamp', 'colourlovers', 'ifttt', 'ebay', 'slack', 'okcupid', 'trip', 'ello', 'tracky', 'basecamp'
        ]
        self.username = str(username)
    
    #def_[return_dframe]
    def return_dframe(self, website_names_for_socket=None, websites=None):
        website_names_for_socket = self.website_names_for_socket
        websites = self.websites
        #counter
        count = int(0)
        print(COLORS.GREEN + '\nwebsites in the search')

        for KEY in website_names_for_socket:
            print(COLORS.GREEN + f'{KEY}: ' + COLORS.RED + str(websites[int(count)]))
            count +=int(1)
     
    #def_[search_web]
    def search_web(self,username=None,websites=None):
        print('\nsearching the web...... ')
        self.counter = int(1)
        username = self.username
        websites = self.websites

        #for_loop
        for media_account in websites:
            results_of_check = requests.get(media_account)
            #if_elifs_else
            if bool(results_of_check) == True:
                print(COLORS.WHITE + 'account found: ' + COLORS.BLUE + '{}'.format(media_account)) 
                self.counter += int(1)
            else:
                pass
    
    #def_[results_banner]
    def results_banner(self,counter=None,username=None):
        counter = int(self.counter)
        username = self.username
        print(COLORS.GREEN + '\nthere are ' + COLORS.BLUE + f'{counter}' + COLORS.GREEN + ' active accounts with the name ' + COLORS.BLUE +  f'{username}')



#def_[EX]
def EX():
    banner()
    ask = int(input('would you like to see all the urls for the search [1==YES] <> [0==NO]: '))

    HLA = hunt_lost_accounts()
    #if_elifs_else
    if bool(ask) == True:
        HLA.return_dframe()
    else:
        pass
    HLA.search_web()
    HLA.results_banner()
    time.sleep(10000)
    print(COLORS.RED + '\nshutting down.........')

#call_functions
EX()
            


