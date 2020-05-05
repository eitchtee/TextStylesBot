import random


def cebolinha(txt):
    txt = txt.replace('\n', ' @¨# ')
    txt = txt.split()

    final_txt = []
    for word in txt:
        word.strip()
        if word == '@¨#':
            word = word.replace('@¨#', '\n')
        else:
            check_word = ''.join([i for i in word if i.isalpha()])
            if len(check_word) >= 1 and \
                    check_word[len(check_word) - 1] != 'r' and \
                    check_word[len(check_word) - 1] != 'R':
                word = word.replace('r', 'l').replace('R', 'L')
            else:
                count_r_down = word.count('r')
                count_r_upper = word.count('R')
                word = word.replace('r', 'l', count_r_down - 1). \
                    replace('R',
                            'L',
                            count_r_upper - 1)

        final_txt.append(word + ' ')

    final_txt = ''.join(final_txt).replace(' \n ', '\n').replace('\n ',
                                                                 '\n').replace(
        ' \n', '\n')

    return final_txt


def upper_and_lower(txt):
    capitalize = 0
    final_txt = []
    for letter in txt:
        if capitalize and letter.isalpha():
            letter = letter.upper()
            capitalize = 0
        elif not capitalize and letter.isalpha():
            letter = letter.lower()
            capitalize = 1

        final_txt.append(letter)

    return ''.join(final_txt)


class Zalgo:
    def __init__(self):
        self.numAccentsUp = (1, 3)
        self.numAccentsDown = (1, 3)
        self.numAccentsMiddle = (1, 2)
        self.maxAccentsPerLetter = 3
        # downward going diacritics
        self.dd = ['̖', ' ̗', ' ̘', ' ̙', ' ̜', ' ̝', ' ̞', ' ̟', ' ̠', ' ̤',
                   ' ̥', ' ̦', ' ̩', ' ̪', ' ̫', ' ̬', ' ̭', ' ̮', ' ̯', ' ̰',
                   ' ̱', ' ̲', ' ̳', ' ̹', ' ̺', ' ̻', ' ̼', ' ͅ', ' ͇', ' ͈',
                   ' ͉', ' ͍', ' ͎', ' ͓', ' ͔', ' ͕', ' ͖', ' ͙', ' ͚', ' ', ]
        # upward diacritics
        self.du = [' ̍', ' ̎', ' ̄', ' ̅', ' ̿', ' ̑', ' ̆', ' ̐', ' ͒', ' ͗',
                   ' ͑', ' ̇', ' ̈', ' ̊', ' ͂', ' ̓', ' ̈́', ' ͊', ' ͋', ' ͌',
                   ' ̃', ' ̂', ' ̌', ' ͐', ' ́', ' ̋', ' ̏', ' ̽', ' ̉', ' ͣ',
                   ' ͤ', ' ͥ', ' ͦ', ' ͧ', ' ͨ', ' ͩ', ' ͪ', ' ͫ', ' ͬ', ' ͭ',
                   ' ͮ', ' ͯ', ' ̾', ' ͛', ' ͆', ' ̚', ]
        # middle diacritics
        self.dm = [' ̕', ' ̛', ' ̀', ' ́', ' ͘', ' ̡', ' ̢', ' ̧', ' ̨', ' ̴',
                   ' ̵', ' ̶', ' ͜', ' ͝', ' ͞', ' ͟', ' ͠', ' ͢', ' ̸', ' ̷',
                   ' ͡', ]

    def zalgofy(self, text):
        # Zalgofy a string
        # get the letters list
        letters = list(text)  # ['t','e','s','t',' ','t',...]
        # print(letters)
        # new_word = ''
        new_letters = []

        # for each letter, add some diacritics of all varieties
        for letter in letters:  # 'p', etc...
            a = letter  # create a dummy letter

            # skip this letter we can't add a diacritic to it
            if not a.isalnum():
                new_letters.append(a)
                continue

            num_accents = 0
            num_u = random.randint(self.numAccentsUp[0], self.numAccentsUp[1])
            num_d = random.randint(self.numAccentsDown[0],
                                   self.numAccentsDown[1])
            num_m = random.randint(self.numAccentsMiddle[0],
                                   self.numAccentsMiddle[1])
            # Try to add accents to the letter, will add an upper, lower,
            # or middle accent randomly until
            # either num_accents == self.maxAccentsPerLetter or we have added
            # the maximum upper, middle and lower accents. Denoted
            # by num_u, num_d, and num_m
            while num_accents < self.maxAccentsPerLetter and num_u + num_m + \
                    num_d != 0:
                randint = random.randint(0,
                                         2)  # randomly choose what accent
                # type to add
                if randint == 0:
                    if num_u > 0:
                        a = self.combine_with_diacritic(a, self.du)
                        num_accents += 1
                        num_u -= 1
                elif randint == 1:
                    if num_d > 0:
                        a = self.combine_with_diacritic(a, self.dd)
                        num_d -= 1
                        num_accents += 1
                else:
                    if num_m > 0:
                        a = self.combine_with_diacritic(a, self.dm)
                        num_m -= 1
                        num_accents += 1

            # a = a.replace(" ","") #remove any spaces, this also gives it
            # the zalgo text look
            # print('accented a letter: ' + a)
            new_letters.append(a)

        new_word = ''.join(new_letters)
        return new_word

    @staticmethod
    def combine_with_diacritic(letter, diacritic_list):
        # Combines letter and a random character from diacriticLis
        return letter.strip() + diacritic_list[
            random.randrange(0, len(diacritic_list))].strip()


def zalgo_txt(txt):
    z = Zalgo()
    z.numAccentsUp = (1, 3)
    z.numAccentsDown = (1, 3)
    z.numAccentsMiddle = (1, 2)
    z.maxAccentsPerLetter = 40

    return z.zalgofy(txt)


def double_struck(txt):
    normal_letters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLM" \
                     "NOPQRSTUVWXYZ"
    double_struck_letter = \
        "𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄" \
        "ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ"

    trantab = txt.maketrans(normal_letters, double_struck_letter)

    txt = txt.translate(trantab)
    return txt


def cursive(txt):
    normal_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLM" \
                     "NOPQRSTUVWXYZ"
    cursive_letter = \
        "𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜" \
        "𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩"

    trantab = txt.maketrans(normal_letters, cursive_letter)

    txt = txt.translate(trantab)
    return txt


def large(txt):
    normal_letters = "`1234567890-=~!@#$%^&*()_+qwertyuiop[]QWERTYUIOP" \
                     "{}|asdfghjkl;'ASDFGHJKL:" \
                     "\\zxcvbnm,./ZXCVBNM<>?"
    fancy_letter = "`１２３４５６７８９０－＝~！＠＃＄％^＆＊（）_＋ｑｗｅｒｔｙｕｉｏｐ" \
                   "[]ＱＷＥＲＴＹＵＩＯＰ{}|ａｓｄｆｇｈｊｋｌ；＇ＡＳＤＦＧＨＪＫＬ：" \
                   "\\ｚｘｃｖｂｎｍ，．／ＺＸＣＶＢＮＭ<>？"

    trantab = txt.maketrans(normal_letters, fancy_letter)

    txt = txt.translate(trantab)
    return txt


def circled(txt):
    normal_letters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcde" \
                     "fghijklmnopqrstuvwxyz"
    fancy_letter = "⓪①②③④⑤⑥⑦⑧⑨ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏⓐⓑⓒⓓⓔ" \
                   "ⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ"

    trantab = txt.maketrans(normal_letters, fancy_letter)

    txt = txt.translate(trantab)
    return txt


def negative_circled(txt):
    normal_letters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcde" \
                     "fghijklmnopqrstuvwxyz"
    fancy_letter = \
        "🄌➊➋➌➍➎➏➐➑➒🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩🅐🅑🅒🅓🅔" \
        "🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩"

    trantab = txt.maketrans(normal_letters, fancy_letter)

    txt = txt.translate(trantab)
    return txt


def parenthesis(txt):
    normal_letters = "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" \
                     "abcdefghijklmnopqrstuvwxyz"
    fancy_letter = \
        "⑴⑵⑶⑷⑸⑹⑺⑻⑼🄐🄑🄒🄓🄔🄕🄖🄗🄘🄙🄚🄛🄜🄝🄞🄟🄠🄡🄢🄣🄤🄥🄦🄧🄨🄩" \
        "⒜⒝⒞⒟⒠⒡⒢⒣⒤⒥⒦⒧⒨⒩⒪⒫⒬⒭⒮⒯⒰⒱⒲⒳⒴⒵"

    trantab = txt.maketrans(normal_letters, fancy_letter)

    txt = txt.translate(trantab)
    return txt


def fraktur(txt):
    normal_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    fancy_letter = \
        "𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷"

    trantab = txt.maketrans(normal_letters, fancy_letter)

    txt = txt.translate(trantab)
    return txt


def leet(txt):
    normal_letters = "tTiIbBoOsSaAeElLzZ"
    fancy_letter = "771188005544331122"

    trantab = txt.maketrans(normal_letters, fancy_letter)

    txt = txt.translate(trantab)
    return txt


def morse_code(txt):
    morse_table = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '0': '-----',
        'À': '.--.-',
        'Ç': '-.-..',
        'È': '.-..-',
        'É': '..-..',
        '.': '.-.-.-',
        ',': '--..--',
        '?': '..--..',
        "'": '.----.',
        '!': '-.-.--',
        '/': '-..-.',
        '(': '-.--.',
        ')': '-.--.-',
        '&': '.-...',
        ':': '---...',
        ';': '-.-.-.',
        '=': '-...-',
        '-': '-....-',
        '_': '..--.-',
        '"': '.-..-.',
        '$': '...-..-',
        '@': '.--.-.'
    }

    txt_words = txt.split()

    encoded_string = []
    index = 0
    for word in txt_words:
        word = word.strip()

        for letter in word:
            try:
                encoded_string.append(morse_table[letter.upper()])
            except KeyError:
                encoded_string.append('#')

        if len(txt_words) > 1 and index < (len(txt_words) - 1):
            encoded_string.append('/')
        index += 1

    return_txt = ' '.join(encoded_string)
    if return_txt:
        return return_txt
    else:
        return ''


def binary(txt):
    binary_result = []
    for s in txt:
        if s == ' ':
            binary_result.append('00100000')
        else:
            binary_result.append(bin(ord(s)))
    return ''.join(str(b_str) for b_str in binary_result).replace('b', '')


def spaced(txt):
    return ' '.join([char.upper() for char in
                     ' '.join(txt.split(sep=None))])


def reverse(txt):
    return txt[::-1]


def strikethrough(txt):
    result = []
    for c in txt:
        result.append(c + '\u0336')
    return '\u0336'.join('\u0336' + txt) + '\u0336'


def small_caps(txt):
    normal_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    fancy_letter = "ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ"

    trantab = txt.maketrans(normal_letters, fancy_letter)

    txt = txt.translate(trantab)
    return txt


def superscript(txt):
    normal_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    fancy_letter = "ᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖᵠʳˢᵗᵘᵛʷˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖᵠʳˢᵗᵘᵛʷˣʸᶻ"

    trantab = txt.maketrans(normal_letters, fancy_letter)

    txt = txt.translate(trantab)
    return txt


def underline(txt):
    result = []
    for c in txt:
        if c.isalnum():
            result.append(c + '\u0332')
        elif c == ' ':
            result.append(c + '\u0332')
        else:
            result.append(c)
    return ''.join(result)
