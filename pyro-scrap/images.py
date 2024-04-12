import random

# CRYPTO
image_binance = [
    'https://s0.rbk.ru/v6_top_pics/media/img/0/33/347022784887330.jpeg',
    'https://cloudfront-us-east-2.images.arcpublishing.com/reuters/JPPRVC3NUVN4XAXFE4DKLGRBW4.jpg',
    'https://cloudfront-us-east-1.images.arcpublishing.com/coindesk/HBCOLR54EJEHBNSZNQK6EV5L2M.jpg',
    'https://cdn.punchng.com/wp-content/uploads/2023/06/05172800/binance-2.jpg',
    'https://cdn.iz.ru/sites/default/files/styles/900x506/public/news-2023-12/20231018_aaa_s197_459.jpg?itok=fleMW1Pe',
    'https://ibmm.ru/image/cache/catalog/image/catalog/news/28,02/binance.webp',
    'https://public.bnbstatic.com/image/cms/blog/20220901/f618ab67-d7a1-4615-8427-aef0e157a72f.png',
]

image_ethereum = [
    'https://thumbor.forbes.com/thumbor/fit-in/900x510/https://www.forbes.com/advisor/wp-content/uploads/2021/03/ethereum-1.jpeg',
    'https://fsr-develop.ru/wp-content/uploads/2023/08/image-342.webp',
    'https://cryptoslate.com/wp-content/uploads/2023/12/ethereum.jpg',
    'https://www.forbesindia.com/media/images/2022/Sep/img_194215_mergebg.jpg',
    'https://www.investopedia.com/thmb/QqrOeYc-l9stwOeJ7JyZx_X2MNU=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/stack-of-ether-coins-with-gold-background-901948904-a546d2200ec44115a4c219bce36f88bf.jpg',
    'https://static.news.bitcoin.com/wp-content/uploads/2024/01/etherss45.jpg',
    'https://img.ixbt.site/live/topics/preview/00/05/54/94/443417833a.webp',
    'https://static.toiimg.com/thumb/msid-87889891,width-1280,height-720,imgsize-258274,resizemode-6,overlay-toi_sw,pt-32,y_pad-40/photo.jpg',
]

image_bitcoin = [
    'https://static4.banki.ru/ugc/90/2c/3f/fe/10991560.jpg',
    'https://www.newsbtc.com/wp-content/uploads/2024/02/Bitcoin_73fcc2.jpeg?fit=929%2C523',
    'https://s28126.pcdn.co/blogs/ask-experian/wp-content/uploads/Bitcoin.jpg.optimal.jpg',
    'https://thumbor.forbes.com/thumbor/fit-in/900x510/https://www.forbes.com/advisor/wp-content/uploads/2021/03/bitcoin_glasses.jpg',
    'https://images.moneycontrol.com/static-mcnews/2021/11/Bitcoin-770x433.jpg?impolicy=website&width=770&height=431',
    'https://cdn.finam.ru/images/publications/1562218/bitcoin1_flickr_949bcf5776.jpg',
    'https://habrastorage.org/r/w780/getpro/habr/upload_files/22b/662/f37/22b662f375235f39e2d2491f76dccdec.jpg',
    'https://live-production.wcms.abc-cdn.net.au/2ee67a586afcd0e0b814919f5c8b7d65?impolicy=wcms_crop_resize&cropH=2813&cropW=5000&xPos=0&yPos=260&width=862&height=485',
    'https://img.gazeta.ru/files3/151/15759151/2022-11-01T060140Z_308640285_RC2TCX9UYR40_RTRMADP_3_FINTECH-CRYPTO-WEEKLY-pic_32ratio_1200x800-1200x800-6283.jpg'
]

image_okex = [
    'https://incrypted.com/wp-content/uploads/2024/02/okx-100.jpg',
    'https://walloftraders.com/blog/wp-content/uploads/2023/02/okx-2.jpg',
    'https://altcoinlog.com/wp-content/uploads/2019/04/OKEX-1.jpg',
    'https://bits.media/upload/resize_cache/webp/iblock/597/birzha_okex_vozobnovila_vyvod_tsifrovykh_aktivov.webp',
    'https://daytradingschool.ru/wp-content/uploads/okex-founder-star-xu.jpg',
    'https://external-preview.redd.it/okx-officially-launches-turkish-crypto-exchange-okx-tr-v0-VXiSPJit9T53LTqTcOZHYnxY3TcjkIGORibA-01_tAU.jpg?width=640&crop=smart&auto=webp&s=abae36be81bd1648dcc65ad7d40e8db762864594',
    'https://bitexpert.io/wp-content/uploads/2024/01/OKB-24.png',
]

image_a16z = [
    'https://thehealthcaretechnologyreport.com/wp-content/uploads/2019/10/a16z.jpg',
    'https://a16z.com/wp-content/themes/a16z/assets/images/opegraph_images/corporate-Yoast-Twitter.jpg',
    'https://cdn.decrypt.co/resize/1024/height/512/wp-content/uploads/2020/04/95079523_164737138247395_5964262702741192704_n-gID_5.jpg',
    'https://tkcdn.tekedia.com/wp-content/uploads/2023/12/12131408/ANDRE-768x511.jpg',
    'https://static.news.bitcoin.com/wp-content/uploads/2022/04/shutterstock_2095228648.jpg',
    'https://investgame.net/wp-content/uploads/2021/04/Screenshot-2021-04-30-at-08.47.40.png',
]

image_ton = [
    'https://miro.medium.com/v2/resize:fit:1200/1*Lh2rc2kYjh7FxmpO4xr2gg.jpeg',
    'https://habrastorage.org/r/w780/webt/iy/bf/gv/iybfgv9fsxmk8lpd1xwbcrin2d4.jpeg',
    'https://static.news.bitcoin.com/wp-content/uploads/2023/11/toner.jpg',
    'https://i.ytimg.com/vi/3O-jnS72gY4/maxresdefault.jpg',
    'https://pbs.twimg.com/media/EFcbS7pUwAEZSz8?format=jpg&name=large',
    'https://cryptocurrency.tech/wp-content/uploads/2019/10/ton-2.png',

]

image_cnbc = [
    'https://advanced-television.com/wp-content/uploads/2022/07/CNBC.jpg',
    'https://image.cnbcfm.com/api/v1/image/105490644-1702329788625-TV_Landing_2_1_CNBC1.png?v=1702329794&w=884&h=442&vtcrop=y',
    'https://cryptodnes.bg/wp-content/uploads/2022/07/1579-5d01315c0c620',
]
image_nvidia = [
    'https://habrastorage.org/r/w780/webt/oc/fc/fg/ocfcfgodgwhjzhza2ljlahxpxcy.jpeg',
    'https://www.marketplace.org/wp-content/uploads/2024/03/Nvidia.jpg?fit=2800%2C1884&w=1200',
    'https://c.files.bbci.co.uk/BBB5/production/_129935084_gettyimages-1258278568.jpg',
    'https://filearchive.cnews.ru/img/news/2022/10/03/nv600.jpg',
    'https://compote.slate.com/images/ad323445-cd7b-495f-ab5b-58f8c0aede41.jpeg?crop=6000%2C4000%2Cx0%2Cy0',
    'https://kz.kursiv.media/wp-content/uploads/2024/02/whatsapp-image-2024-02-05-at-2.29.27-pm-1-1280x960.jpeg',
    'https://www.bleepstatic.com/content/hl-images/2022/03/01/NVIDIA___headpic.jpg'
]

image_open_ai = [
    'https://myexeed.com/wp-content/uploads/2023/10/11.webp',
    'https://3dnews.ru/assets/external/illustrations/2023/05/23/1087205/twitter.jpg',
    'https://p-news-upload.storage.googleapis.com/2023/05/GettyImages-1240407936-scaled.jpg',
    'https://overclockers.ru/st/legacy/blog/428111/486923_O.jpg',
    'https://community.intersystems.com/sites/default/files/inline/images/openai-logo.jpg',
    'https://media.wired.com/photos/6567e505b38d7a2373721a81/master/pass/Sam-Altman-OpenAI-Microsoft-Board-Business-1778707567.jpg',
    'https://www.gzeromedia.com/media-library/openai-logo-seen-in-illustration.jpg?id=50581275&width=1200&height=800&quality=85&coordinates=0%2C0%2C0%2C0',
]

image_larry_fink = [
    'https://assets.bwbx.io/images/users/iqjWHBFdfxIU/ilIDOxQF9hso/v0/-1x-1.jpg',
    'https://blockworks-co.imgix.net/wp-content/uploads/2023/10/Larry-Fink-BlackRock-CEO-2.jpg',
    'https://imageio.forbes.com/specials-images/imageserve/61e72f9ba60ce1d0b0028b6a/One-Planet-Summit/0x0.jpg?format=jpg&crop=2972,1981,x0,y44,safe&width=960',
    'https://www.bnnbloomberg.ca/polopoly_fs/1.2051645!/fileimage/httpImage/image.jpg_gen/derivatives/landscape_620/larry-fink.jpg',
    'https://media.vanityfair.com/photos/54cc03023c894ccb27c877b3/master/w_1600%2Cc_limit/image.jpg'
]

image_black_rock = [
    'https://www.aljazeera.com/wp-content/uploads/2022/01/382921463.jpg?resize=1800%2C1800',
    'https://cdn.forbes.ru/forbes-static/new/2022/01/1-GettyImages-1235877214-61e1a137cb543.jpg',
    'https://cdn-kz.kursiv.media/wp-content/uploads/2023/04/shutterstock_2231941451.jpg',
    'https://cloudfront-us-east-2.images.arcpublishing.com/reuters/ESEAURQH2JPBJBUTHNOUHAKCTU.jpg',
    'https://a57.foxnews.com/static.foxbusiness.com/foxbusiness.com/content/uploads/2020/07/1024/512/Larry-Fink-BlackRock-Getty.png?ve=1&tl=1',
    'https://i.ytimg.com/vi/ga_we_sOopk/sddefault.jpg',
    'https://www.investopedia.com/thmb/m4jsTOeRg-AmRdSqNSMm1nLs69M=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-1441467099-6fea6e81a2454f10ab5c34c9d0fe5bd9.jpg',
    'https://aperture.gg/cdn/shop/articles/Blackrock_YT_Thumb_A_1200x1200.jpg?v=1683656355'
]

image_bitfinex = [
    'https://admin.iamforextrader.com/wp-content/uploads/2020/07/bitfinex.png',
    'https://forklog.com/wp-content/uploads/bitfinex-blue.webp',
    'https://hashtelegraph.com/wp-content/uploads/2018/10/bitfinex-tether-bitcoin-scanda1l.jpg',
    'https://cryptoslate.com/wp-content/uploads/2021/09/bitfinex-23m-fee-.jpg',
    'https://incrypted.com/wp-content/uploads/2023/08/Bitfinex_-768x473.jpg',
    'https://cryptoslate.com/wp-content/uploads/2023/10/bitfinex-.jpg',
    'https://www.bnnbloomberg.ca/polopoly_fs/1.1982773!/fileimage/httpImage/image.jpg_gen/derivatives/landscape_620/the-bitfinex-logo-on-a-smartphone-arranged-in-the-brooklyn-borough-of-new-york-u-s-on-monday-may-24-2021-elon-musk-continued-to-toy-with-the-price-of-bitcoin-monday-taking-to-twitter-to-indicate-support-for-what-he-says-is-an-effort-by-miners-to-make-their-operations-greener-photographer-gabby-jones-bloomberg.jpg',
    'https://crypto-economy.com//wp-content/uploads/2024/01/bitfinex-featured-1-1024x576.jpg',
    'https://d.ibtimes.com/en/full/4471462/1.png?w=1600&h=900&q=88&f=e3078a19d90b5c117b225d827a11a158',
]
image_coinbase = [
    'https://www.bankrate.com/2021/09/07122021/GettyImages-1234552839.jpg?auto=webp&optimize=high',
    'https://nypost.com/wp-content/uploads/sites/2/2021/06/sized-coinbase.jpg?quality=75&strip=all',
    'https://media.npr.org/assets/img/2021/04/14/gettyimages-1232311500_custom-1e512eeb19ccf489e2f19fc7d2a1c76783b22c01.jpg',
    'https://cloudfront-us-east-2.images.arcpublishing.com/reuters/72FKU65OXRNLDCBNABLNIXWCAQ.jpg',
    'https://www.tbstat.com/wp/uploads/2023/04/20230419_Coinbase_Generic3-1200x675.jpg',
]

# WORDS

binance_words = ['Binance']
ethereum_words = ['Ethereum']
bitcoin_words = ['Bitcoin', 'btc']
okex_words = ['Okex', 'Okx']
a16z_words = ['a16z', 'Andreessen Horowitz']
ton_words = ['Telegram Open Network', 'Telegram']
cnbc_words = ['CNBC']
nvidia_words = ['Nvidia', 'NVDA']
larry_fink_words = ['Larry Fink']
black_rock_words = ['Black Rock']
bitfinex_words = ['Bitfinex']
coinbase_words = ['Coinbase']

# All dicts
image_dicts_crypto = [
    {
        'words': a16z_words,
        'images': image_a16z
    },
    {
        'words': binance_words,
        'images': image_binance
    },
    {
        'words': okex_words,
        'images': image_okex
    },
    {
        'words': bitcoin_words,
        'images': image_bitcoin
    },
    {
        'words': ethereum_words,
        'images': image_ethereum
    },
    {
        'words': ton_words,
        'images': image_ton
    },
    {
        'words': cnbc_words,
        'images': image_cnbc
    },
    {
        'words': nvidia_words,
        'images': image_nvidia
    },
    {
        'words': larry_fink_words,
        'images': image_larry_fink
    },
    {
        'words': black_rock_words,
        'images': image_black_rock
    },
    {
        'words': bitfinex_words,
        'images': image_bitfinex
    },
    {
        'words': coinbase_words,
        'images': image_coinbase
    }

]
