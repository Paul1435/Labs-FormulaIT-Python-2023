# TODO Найдите количество книг, которое можно разместить на дискете
floppy_disk_volume = 1.44
floppy_disk_volume_byte = 1.44 * 1024 * 1024
count_page = 100
count_str = 50
count_symbol = 25
character_size_bytes = 4
book_size_bytes = count_page * count_str * count_symbol * character_size_bytes
count_books = int(floppy_disk_volume_byte // book_size_bytes)
print("Количество книг, помещающихся на дискету:", count_books)
