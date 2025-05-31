import os
import django
import random
from datetime import timedelta
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User

# Django sozlamalarini o'rnatish
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news.settings')
django.setup()

# Modellarni import qilish
from app.models import Category, Tag, Blog, Comment

def malumot_qosh():
    # Foydalanuvchilar yaratish
    users = []
    for i in range(1, 10):
        user, created = User.objects.get_or_create(
            username=f'foydalanuvchi{i}',
            defaults={'password': 'parol123', 'email': f'foydalanuvchi{i}@example.com'}
        )
        
        users.append(user)

    # Kategoriyalar (inglizcha, o'zbekcha, ruscha nomlar bilan)
    category_names = [
        ('politics', 'Siyosat', 'Политика'),
        ('technology', 'Texnologiya', 'Технологии'),
        ('gadgets', 'Gadjet', 'Гаджеты'),
        ('travel', 'Sayohat', 'Путешествия'),
        ('business', 'Biznes', 'Бизнес'),
        ('sport', 'Sport', 'Спорт'),
        ('life-style', 'Turmush tarzi', 'Стиль жизни')
    ]
    categories = []
    for en_name, uz_name, ru_name in category_names:
        category, _ = Category.objects.get_or_create(slug=slugify(en_name))
        category.set_current_language('en')
        category.name = en_name
        category.set_current_language('uz')
        category.name = uz_name
        category.set_current_language('ru')
        category.name = ru_name
        category.save()
        categories.append(category)

    # Teglar (inglizcha, o'zbekcha, ruscha)
    tag_names = [
        ('Breaking News', 'So\'nggi yangiliklar', 'Срочные новости'),
        ('Innovation', 'Innovatsiya', 'Инновации'),
        ('Trending', 'Trend', 'Тренды'),
        ('Adventure', 'Sarguzasht', 'Приключения'),
        ('Finance', 'Moliya', 'Финансы'),
        ('Health', 'Salomatlik', 'Здоровье'),
        ('Fitness', 'Fitnes', 'Фитнес'),
        ('Culture', 'Madaniyat', 'Культура')
    ]
    tags = []
    for en_name, uz_name, ru_name in tag_names:
        tag, _ = Tag.objects.get_or_create()
        tag.set_current_language('en')
        tag.name = en_name
        tag.set_current_language('uz')
        tag.name = uz_name
        tag.set_current_language('ru')
        tag.name = ru_name
        tag.save()
        tags.append(tag)

    # Blog sarlavhalari (inglizcha, o'zbekcha, ruscha)
    blog_titles = {
        'politics': [
            ('New Policy Sparks Debate in Parliament', 'Yangi siyosat parlamentda bahs-munozaraga sabab bo\'ldi', 'Новая политика вызвала дебаты в парламенте'),
            ('Election Results Shape National Future', 'Saylov natijalari milliy kelajakni shakllantiradi', 'Результаты выборов формируют будущее страны'),
            ('Global Summit Addresses Climate Crisis', 'Global sammit iqlim inqirozini muhokama qildi', 'Глобальный саммит обсуждает климатический кризис'),
            ('Trade Agreement Faces Opposition', 'Savdo kelishuvi qarshilikka duch keldi', 'Торговое соглашение сталкивается с сопротивлением'),
            ('Legislation Reform Gains Momentum', 'Qonunchilik islohoti jadal davom etmoqda', 'Реформа законодательства набирает обороты'),
            ('Diplomatic Talks Ease Tensions', 'Diplomatik muzokaralar keskinlikni yumshatdi', 'Дипломатические переговоры смягчают напряжение'),
            ('Budget Plan Under Scrutiny', 'Byudjet rejasi sinchkovlik bilan tekshirilmoqda', 'План бюджета находится под пристальным вниманием'),
            ('Political Rally Draws Thousands', 'Siyosiy miting minglab odamlarni jalb qildi', 'Политический митинг привлек тысячи людей'),
            ('New Law Impacts Local Communities', 'Yangi qonun mahalliy jamoalarga ta\'sir qildi', 'Новый закон влияет на местные сообщества'),
            ('International Relations at Crossroads', 'Xalqaro munosabatlar chorrahasida', 'Международные отношения на перепутье')
        ],
        'technology': [
            ('AI Breakthrough Revolutionizes Industry', 'Sun\'iy intellekt sohada inqilob qildi', 'Прорыв в ИИ революционизирует индустрию'),
            ('Quantum Computing Milestone Achieved', 'Kvant hisoblashda muhim yutuqqa erishildi', 'Достигнут важный этап в квантовых вычислениях'),
            ('5G Rollout Accelerates Globally', '5G global miqyosda jadal joriy etilmoqda', 'Внедрение 5G ускоряется по всему миру'),
            ('Cybersecurity Threats on the Rise', 'Kiberxavfsizlik tahdidlari ortib bormoqda', 'Угрозы кибербезопасности растут'),
            ('Blockchain Adoption Grows Rapidly', 'Blokcheyn qabul qilinishi tez sur\'atda o\'smoqda', 'Принятие блокчейна быстро растет'),
            ('Tech Giants Unveil New Platforms', 'Texnologiya gigantlari yangi platformalarni taqdim etdi', 'Технологические гиганты представили новые платформы'),
            ('Cloud Computing Trends for 2025', '2025 yil uchun bulutli hisoblash tendentsiyalari', 'Тенденции облачных вычислений на 2025 год'),
            ('Virtual Reality Gets Major Upgrade', 'Virtual haqiqat katta yangilanish oldi', 'Виртуальная реальность получила крупное обновление'),
            ('Open-Source Movement Gains Traction', 'Ochiq kod harakati ommalashmoqda', 'Движение за открытый код набирает популярность'),
            ('Data Privacy Laws Tighten', 'Ma\'lumotlar maxfiyligi qonunlari qattiqlashmoqda', 'Законы о конфиденциальности данных ужесточаются')
        ],
        'gadgets': [
            ('Latest Smartphone Boasts Stunning Features', 'So\'nggi smartfon ajoyib xususiyatlarga ega', 'Новейший смартфон обладает потрясающими функциями'),
            ('Smartwatch Tracks Health Like Never Before', 'Aqlli soat sog\'liqni ilgari bo\'lmagan tarzda kuzatadi', 'Умные часы отслеживают здоровье как никогда раньше'),
            ('Wireless Earbuds Redefine Audio', 'Simsiz quloqchinlar audio tajribasini qayta belgilaydi', 'Беспроводные наушники переопределяют аудио'),
            ('Foldable Screens Hit the Market', 'Bukiladigan ekranlar bozorga chiqdi', 'Складные экраны появились на рынке'),
            ('New Drone Offers Advanced Capabilities', 'Yangi dron ilg\'or imkoniyatlarni taklif qiladi', 'Новый дрон предлагает продвинутые возможности'),
            ('Gaming Console Breaks Sales Records', 'O\'yin konsoli sotuv rekordlarini yangiladi', 'Игровая консоль бьет рекорды продаж'),
            ('Smart Home Devices Get Smarter', 'Aqlli uy qurilmalari yanada aqlliroq bo\'lmoqda', 'Умные домашние устройства становятся умнее'),
            ('Wearable Tech Trends for 2025', '2025 yil uchun kiyiladigan texnologiya tendentsiyalari', 'Тенденции носимых технологий на 2025 год'),
            ('Camera Tech Revolutionizes Photography', 'Kamera texnologiyasi fotografiyada inqilob qildi', 'Технология камер революционизирует фотографию'),
            ('Portable Chargers Get a Boost', 'Portativ zaryadlovchilar yangi imkoniyatlarga ega', 'Портативные зарядные устройства получили улучшения')
        ],
        'travel': [
            ('Top Destinations for 2025 Revealed', '2025 yil uchun eng yaxshi sayohat yo\'nalishlari e\'lon qilindi', 'Лучшие направления путешествий на 2025 год объявлены'),
            ('Eco-Friendly Travel Gains Popularity', 'Ekologik sayohat ommalashmoqda', 'Экологичные путешествия набирают популярность'),
            ('Hidden Gems for Adventure Seekers', 'Sarguzasht izlovchilar uchun yashirin joylar', 'Скрытые жемчужины для искателей приключений'),
            ('Luxury Resorts Open New Locations', 'Hashamatli kurortlar yangi joylarda ochilmoqda', 'Роскошные курорты открывают новые локации'),
            ('Travel Restrictions Ease Globally', 'Sayohat cheklovlari global miqyosda yumshatildi', 'Ограничения на поездки смягчаются по всему миру'),
            ('Cultural Festivals Draw Tourists', 'Madaniy festivallar sayyohlarni jalb qilmoqda', 'Культурные фестивали привлекают туристов'),
            ('Backpacking Trends for Young Travelers', 'Yosh sayohatchilar uchun ryukzak sayohati tendentsiyalari', 'Тенденции рюкзачных путешествий для молодежи'),
            ('Cruise Industry Makes a Comeback', 'Kruiz industriyasi qayta tiklanmoqda', 'Круизная индустрия возвращается'),
            ('Solo Travel Safety Tips Shared', 'Yakka sayohat uchun xavfsizlik maslahatlari ulashildi', 'Советы по безопасности для одиночных путешествий'),
            ('Sustainable Tourism Initiatives Launched', 'Barqaror turizm tashabbuslari boshlandi', 'Инициативы устойчивого туризма запущены')
        ],
        'business': [
            ('Stock Market Hits Record High', 'Fond bozori rekord darajaga chiqdi', 'Фондовый рынок достиг рекордного уровня'),
            ('Startup Secures Massive Funding', 'Startap katta moliyaviy yordam oldi', 'Стартап получил крупное финансирование'),
            ('Corporate Mergers Shake Industry', 'Korporativ birlashmalar sohani larzaga keltirdi', 'Корпоративные слияния потрясли индустрию'),
            ('Supply Chain Issues Persist', 'Ta\'minot zanjiri muammolari davom etmoqda', 'Проблемы с цепочками поставок сохраняются'),
            ('Entrepreneurship Trends for 2025', '2025 yil uchun tadbirkorlik tendentsiyalari', 'Тенденции предпринимательства на 2025 год'),
            ('Global Trade Faces New Challenges', 'Global savdo yangi muammolarga duch kelmoqda', 'Глобальная торговля сталкивается с новыми вызовами'),
            ('Tech Unicorns Dominate Markets', 'Texnologik yakkashoxlar bozorni egallamoqda', 'Технологические единороги доминируют на рынках'),
            ('Retail Sector Adapts to Trends', 'Chakana savdo sohasi tendentsiyalarga moslashmoqda', 'Розничный сектор адаптируется к трендам'),
            ('Investment Strategies for Beginners', 'Yangi investorlar uchun sarmoya strategiyalari', 'Инвестиционные стратегии для новичков'),
            ('Economic Forecast Predicts Growth', 'Iqtisodiy prognoz o\'sishni bashorat qilmoqda', 'Экономический прогноз предсказывает рост')
        ],
        'sport': [
            ('Team Wins Championship in Thriller', 'Jamoa hayajonli o\'yinda chempionlikni qo\'lga kiritdi', 'Команда выиграла чемпионат в захватывающей игре'),
            ('Athlete Breaks World Record', 'Sportchi jahon rekordini yangiladi', 'Спортсмен побил мировой рекорд'),
            ('New Stadium Opens to Fans', 'Yangi stadion muxlislar uchun ochildi', 'Новый стадион открыт для болельщиков'),
            ('Sports Tech Enhances Performance', 'Sport texnologiyasi ishlashni yaxshilaydi', 'Спортивные технологии улучшают производительность'),
            ('Olympic Preparations Underway', 'Olimpiada tayyorgarligi davom etmoqda', 'Подготовка к Олимпиаде продолжается'),
            ('Underdog Team Shocks Favorites', 'Kutilmagan jamoa favoritlarni hayratda qoldirdi', 'Команда-аутсайдер шокировала фаворитов'),
            ('Fitness Trends Shape Training', 'Fitnes tendentsiyalari mashg\'ulotlarni shakllantiradi', 'Фитнес-тренды формируют тренировки'),
            ('E-Sports Gains Mainstream Appeal', 'E-sport ommaviy e\'tirofga sazovor bo\'lmoqda', 'Киберспорт становится популярным'),
            ('Injury Prevention Tech Advances', 'Jarohatlarni oldini olish texnologiyasi rivojlanmoqda', 'Технологии предотвращения травм развиваются'),
            ('Marathon Events Draw Crowds', 'Marafon tadbirlari olomonni jalb qilmoqda', 'Марафонские мероприятия привлекают толпы')
        ],
        'life-style': [
            ('Minimalist Living Trends Grow', 'Minimalistik hayot tarzi tendentsiyalari o\'smoqda', 'Тенденции минималистичного образа жизни растут'),
            ('Vegan Recipes Take Social Media by Storm', 'Vegan retseptlari ijtimoiy tarmoqlarni zabt etmoqda', 'Веганские рецепты захватывают социальные сети'),
            ('Home Decor Ideas for 2025', '2025 yil uchun uy bezash g\'oyalari', 'Идеи декора дома на 2025 год'),
            ('Wellness Retreats Gain Popularity', 'Sog\'lomlashtirish dam olish maskanlari ommalashmoqda', 'Оздоровительные ретриты набирают популярность'),
            ('Sustainable Fashion Makes Waves', 'Barqaror moda katta to\'lqinlar yasamoqda', 'Устойчивая мода вызывает волну'),
            ('Mindfulness Apps See Surge', 'Ongli hayot ilovalari ommalashmoqda', 'Приложения для осознанности набирают популярность'),
            ('DIY Projects Inspire Creativity', 'O\'z qo\'llaringiz bilan loyihalar ijodkorlikni ilhomlantiradi', 'Проекты своими руками вдохновляют на творчество'),
            ('Pet Adoption Rates Soar', 'Uy hayvonlarini asrab olish darajasi keskin oshdi', 'Уровень усыновления домашних животных резко возрос'),
            ('Urban Gardening Trends Rise', 'Shahar bog\'dorchiligi tendentsiyalari o\'smoqda', 'Тенденции городского садоводства растут'),
            ('Self-Care Routines Redefined', 'O\'z-o\'ziga g\'amxo\'rlik odatlari qayta belgilandi', 'Ритуалы заботы о себе переосмыслены')
        ]
    }

    # Blog uchun namunaviy matn (uchta tilda)
    sample_text = {
        'en': (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
            "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
        ),
        'uz': (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Bu matn namunaviy ma'lumot sifatida ishlatiladi. "
            "Maqola mazmuni haqida qisqacha ma'lumot beradi va sayt sinovi uchun foydalaniladi."
        ),
        'ru': (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Этот текст используется как пример данных. "
            "Он предоставляет краткую информацию о содержании статьи и используется для тестирования сайта."
        )
    }

    # Bloglar va izohlar yaratish
    for category in categories:
        category_name = category.safe_translation_getter('name', language_code='en')
        for i in range(10):
            # Blog obyektini yaratish (lekin hali saqlamaymiz)
            blog = Blog(
                category=category,
                status=Blog.StatusEnum.PUBLISHED if i % 2 == 0 else Blog.StatusEnum.DRAFT,
                datetime=timezone.now() - timedelta(days=i)
            )
            # Tarjimalarni o'rnatish
            blog.set_current_language('en')
            blog.title = blog_titles[category_name][i][0]
            blog.text = f"{blog_titles[category_name][i][0]}\n\n{sample_text['en']}"
            blog.set_current_language('uz')
            blog.title = blog_titles[category_name][i][1]
            blog.text = f"{blog_titles[category_name][i][1]}\n\n{sample_text['uz']}"
            blog.set_current_language('ru')
            blog.title = blog_titles[category_name][i][2]
            blog.text = f"{blog_titles[category_name][i][2]}\n\n{sample_text['ru']}"
            # Endi saqlaymiz
            blog.save()
            # Bog'lanishlarni o'rnatish
            blog.tags.set(random.sample(tags, k=random.randint(1, 3)))
            blog.like.set(random.sample(users, k=random.randint(0, 3)))
            blog.seen.set(random.sample(users, k=random.randint(1, 4)))

            # Har bir blog uchun 1-2 izoh (o'zbekcha)
            for j in range(random.randint(1, 2)):
                Comment.objects.create(
                    user=random.choice(users),
                    blog=blog,
                    text=f"{blog_titles[category_name][i][1]} haqida {j+1}-izoh: Ajoyib maqola!",
                    time=timezone.now() - timedelta(hours=j)
                )

    print("Namunaviy ma'lumotlar muvaffaqiyatli qo'shildi!")