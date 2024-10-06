from scrapper import get_article_info

business = [
    "https://www.thehindu.com/business/swiggy-files-papers-with-sebi-for-ipo/article68691431.ece",
    "https://www.thehindu.com/business/consumer-sentiment-for-buying-festive-clothes-remain-weak-cmai-survey/article68690859.ece",
    "https://www.thehindu.com/business/vietnam-coffee-prices-fall-ahead-of-new-harvest/article68689104.ece",
    "https://www.thehindu.com/business/lupins-api-finished-product-facility-in-mp-gets-us-fda-observations/article68694927.ece",
    "https://www.thehindu.com/business/us-fda-issues-4-observations-to-biocon-api-facility-in-bengaluru/article68694933.ece",
    "https://www.thehindu.com/business/dr-reddys-invests-620-mn-in-swiss-arm-to-acquire-haleons-nicotinell-portfolio/article68694917.ece",
    "https://www.thehindu.com/business/shriram-life-aiming-at-threefold-growth-in-annual-premium-equivalent-by-fy30/article68694409.ece",
    "https://www.thehindu.com/news/national/andhra-pradesh/ap-genco-and-nphc-sign-pact-for-development-of-renewable-energy-projects/article68693421.ece",
    "https://www.thehindu.com/news/international/germanys-beer-sector-relies-on-education-to-combat-climate-change/article68690522.ece",
    "https://www.thehindu.com/business/Economy/centre-exempts-non-basmati-white-rice-from-export-duty-cuts-levy-on-parboiled-rice/article68693428.ece"
]

entertainment = [
    "https://www.thehindu.com/entertainment/movies/iifa-2024-awards-celebrities-speak-on-hema-committee-report-and-womens-safety/article68693832.ece",
    "https://www.thehindu.com/entertainment/movies/binny-and-family-movie-review-anjini-dhawan-and-pankaj-kapur-bridge-the-generation-gap-in-this-heartfelt-family-drama/article68690117.ece",
    "https://www.thehindu.com/entertainment/movies/love-sitara-movie-review-pre-wedding-blues-with-sobhita-dhulipala/article68689328.ece",
    "https://www.thehindu.com/entertainment/movies/why-the-bad-guy-from-baahubali-is-distributing-payal-kapadias-all-we-imagine-as-light/article68673934.ece",
    "https://www.thehindu.com/entertainment/movies/love-sitara-movie-review-pre-wedding-blues-with-sobhita-dhulipala/article68689328.ece",
    "https://www.thehindu.com/entertainment/movies/thandakaaranyam-first-look-of-gundu-directors-next-produced-by-pa-ranjith-out/article68694326.ece",
    "https://www.thehindu.com/entertainment/movies/screen-share-films-that-speak-of-homecoming/article68676816.ece",
    "https://www.thehindu.com/entertainment/movies/ramayana-the-legend-of-prince-rama-to-release-in-india-with-new-dubs/article68694124.ece",
    "https://www.thehindu.com/entertainment/movies/manjummel-boys-to-compete-at-russias-kinobravo-film-festival/article68694142.ece",
    "https://www.thehindu.com/entertainment/movies/will-harper-review-will-ferrell-and-harper-steeles-documentary-explores-friendship-acceptance-and-self-discovery/article68693930.ece"
]

lifestyle = [
    "https://www.thehindu.com/life-and-style/fashion/nayaab-brings-23-fashion-brands-that-are-reviving-heritage-textile-techniques-to-chennai/article68681158.ece",
    "https://www.thehindu.com/life-and-style/fashion/manish-malhotra-becomes-the-first-indian-designer-to-showcase-his-fashion-line-world-collection-at-harrods-london/article68685649.ece",
    "https://www.thehindu.com/entertainment/music/brillante-piano-festival-brings-harmonies-in-ebony-and-ivory-to-bengaluru/article68676590.ece",
    "https://www.thehindu.com/life-and-style/chennai-designer-neesha-amrishs-handmade-stoles-are-now-at-the-van-gogh-museum-store-in-amsterdam/article68677611.ece",
    "https://www.thehindu.com/life-and-style/chennai-attend-this-symposium-of-art-science-and-knowledge-to-learn-from-the-experts-of-the-commons/article68676604.ece",
    "https://www.thehindu.com/life-and-style/five-years-and-counting-maya-bazaar-is-back-in-bengaluru-this-weekend/article68660366.ece",
    "https://www.thehindu.com/life-and-style/at-the-brand-new-madras-international-karting-arena-drive-on-the-track-that-mika-hakkinen-narain-karthikeyan-and-karun-chandhok-raced-on/article68673083.ece",
    "https://www.thehindu.com/life-and-style/dancer-methil-devika-makes-her-feature-film-debut-with-the-malayalam-film-kadha-innuvare/article68655177.ece",
    "https://www.thehindu.com/life-and-style/chennai-for-madras-busking-it-is-all-about-conversations-and-memories/article68650921.ece",
    "https://www.thehindu.com/life-and-style/chettinad-cultural-festival-meenakshi-meyyappan-third-edition-karaikudi/article68651620.ece"
]

society = [
    "https://www.thehindu.com/entertainment/art/tribute-remembering-visionary-artist-hanif-kureshi-who-took-art-to-indias-streets/article68681498.ece",
    "https://www.thehindu.com/entertainment/art/the-wonderful-calligraphy-koeli-mukherjee-chronicles-the-artistry-of-parameshwar-raju/article68673406.ece",
    "https://www.thehindu.com/society/india-woman-politician-balance-ambitions-identity-expectations-mamata-banerjee-atishi-vinesh-phogat/article68676929.ece",
    "https://www.thehindu.com/news/cities/Coimbatore/meet-coimbatore-artisan-who-makes-clay-golu-dolls/article68684901.ece",
    "https://www.thehindu.com/news/cities/Coimbatore/learn-to-weave-from-weavers-themselves-at-chennimalais-nurpu-handloom-collective/article68651290.ece",
    "https://www.thehindu.com/society/satire-bananas-in-new-india-g-sampath-column-old-society/article68676771.ece",
    "https://www.thehindu.com/entertainment/art/hyderabad-based-theatre-group-the-torn-curtains-to-stage-a-play-at-the-park-in-visakhapatnam/article68680560.ece",
    "https://www.thehindu.com/entertainment/art/divya-kala-mela-in-visakhapatnam-showcases-talents-of-differently-abled-entrepreneurs-from-across-india/article68684937.ece",
    "https://www.thehindu.com/books/international-translation-day-2024-change-challenges-publishing-industry-young-new-talent-role-of-ai/article68677721.ece"
]

technology = [
    "https://www.thehindu.com/sci-tech/technology/apple-drops-out-of-talks-to-join-openai-investment-round/article68693533.ece",
    "https://www.thehindu.com/sci-tech/technology/cisco-inaugurates-manufacturing-facility-near-chennai-aiming-to-power-more-than-13-billion-in-revenue/article68690294.ece",
    "https://www.thehindu.com/sci-tech/technology/openai-sees-116-billion-revenue-next-year-offers-thrive-chance-to-invest-again-in-2025/article68693620.ece",
    "https://www.thehindu.com/sci-tech/technology/nvidias-geforce-rtx-ai-pc-tour-shows-more-immersive-future-of-gaming/article68690250.ece",
    "https://www.thehindu.com/sci-tech/technology/apple-must-face-narrowed-privacy-lawsuit-over-its-apps/article68693585.ece",
    "https://www.thehindu.com/sci-tech/technology/trump-says-he-will-seek-googles-prosecution-if-he-wins-election/article68693561.ece",
    "https://www.thehindu.com/sci-tech/technology/eu-privacy-regulator-fines-meta-91-million-euros-over-password-storage/article68693514.ece",
    "https://www.thehindu.com/sci-tech/technology/gadgets/samsung-galaxy-tab-s10-ultra-and-tab-s10-launched-in-india-price-features-availability/article68689384.ece",
    "https://www.thehindu.com/sci-tech/technology/apple-must-face-narrowed-privacy-lawsuit-over-its-apps/article68693585.ece",
    "https://www.thehindu.com/sci-tech/technology/matt-mullenweg-wordpress-wp-engine-controversy-explained/article68693366.ece",
    "https://www.thehindu.com/sci-tech/technology/gadgets/motorola-edge-50-neo-review-elevated-smartphone-experience-without-stretching-budget/article68689866.ece"
]

sports = [
    "https://www.thehindu.com/sport/cricket/musheer-khan-stable-after-road-accident-but-set-to-miss-irani-cup-initial-ranji-games/article68693978.ece",
    "https://www.thehindu.com/sport/cricket/india-bangladesh-second-test-day-2-updates/article68693394.ece",
    "https://www.thehindu.com/sport/tennis/wada-appeals-to-cas-against-jannik-sinner-doping-verdict-seeks-suspension/article68693830.ece",
    "https://www.thehindu.com/sport/cricket/succession-plan-likely-to-be-discussed-on-the-sidelines-of-bcci-agm/article68694684.ece",
    "https://www.thehindu.com/sport/cricket/indian-squad-for-t20-internationals-against-bangladesh/article68695513.ece",
    "https://www.thehindu.com/sport/football/epl-cole-palmer-scores-4-goals-in-chelsea-win-over-brighton-arsenal-leaves-it-late-to-beat-leicester/article68695482.ece",
    "https://www.thehindu.com/sport/cricket/indian-premier-league-2025-franchises-can-retain-up-to-five-players-with-no-restriction-on-nationality/article68695371.ece",
    "https://www.thehindu.com/sport/hockey/ioc-draws-with-ncoe-railways-thrashes-tn/article68686406.ece",
    "https://www.thehindu.com/sport/hockey/railways-enters-semifinals-with-a-hard-fought-win-over-bpcl/article68682810.ece",
    "https://www.thehindu.com/sport/hockey/we-showed-great-resilience-and-teamwork-in-pro-league-says-harmanpreet/article68273152.ece"
]

education = [
    "https://www.thehindu.com/education/three-iims-isb-hyderabad-among-worlds-top-100-for-mba-courses-qs-rankings/article68681803.ece",
    "https://www.thehindu.com/education/why-a-holistic-education-is-important-in-todays-world/article68666955.ece",
    "https://www.thehindu.com/education/private-engineering-colleges-in-karnataka-demand-more-than-prescribed-fee-for-government-quota-seats/article68685741.ece",
    "https://www.thehindu.com/education/yash-chopra-foundation-launches-scholarship-program-for-children-of-film-workers/article68689839.ece",
    "https://www.thehindu.com/news/national/karnataka/bengaluru-colleges-see-good-placement-with-recruitment-salary-packages-going-up/article68681756.ece",
    "https://www.thehindu.com/news/national/tamil-nadu/inclusive-learning-will-help-bridge-the-rural-urban-divide-says-anil-kakodkar/article68677833.ece",
    "https://www.thehindu.com/education/careers/avtar-announces-6th-edition-of-myavtar-job-fair-for-women/article68676803.ece",
    "https://www.thehindu.com/education/how-educational-institutions-can-help-students-disconnect-from-digital-devices/article68667107.ece",
    "https://www.thehindu.com/education/why-a-holistic-education-is-important-in-todays-world/article68666955.ece",
    "https://www.thehindu.com/education/private-engineering-colleges-in-karnataka-demand-more-than-prescribed-fee-for-government-quota-seats/article68685741.ece"
]

def dump():
    from db import hindu

    for article in business:
        info = get_article_info(article)
        hindu.insert_one(info)

    for article in entertainment:
        info = get_article_info(article)
        hindu.insert_one(info)

    for article in lifestyle:
        info = get_article_info(article)
        hindu.insert_one(info)

    for article in society:
        info = get_article_info(article)
        hindu.insert_one(info)

    for article in technology:
        info = get_article_info(article)
        hindu.insert_one(info)

    for article in sports:
        info = get_article_info(article)
        hindu.insert_one(info)

    for article in education:
        info = get_article_info(article)
        hindu.insert_one(info)

dump()