from typing import List, Dict
import re


def cek_hp(caption):
    hasil = re.findall(
        r'\(?(?:\+62|62|0)(?:\d{2,3})?\)?[ .-]?\d{2,4}[ .-]?\d{2,4}[ .-]?\d{2,4}', caption)

    if len(hasil) > 0:
        return ' '.join(hasil)
    else:
        return None

def cek_email(caption):
    hasil = re.findall(r'[\w\.-]+@[\w\.-]+(\.[\w]+)+', caption)
    if len(hasil) > 0:
        return ' '.join(hasil)
    else:
        return None