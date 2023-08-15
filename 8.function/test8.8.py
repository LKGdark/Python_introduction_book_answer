def make_album(singer_name,album_name,num = None):
    """打印歌手的专辑和其他内容"""
    album = {
        's_name':singer_name,
        'a_name':album_name,
    }
    if num:
        album['num'] = num
    return album
choice = 'False'
num = None
while True:
    print("Input singer name and album_name")
    print("(press 'quit' any time while you want to go out)\n")

    singer_name = input("input singer name:")
    if singer_name == 'quit':
        break
    album_name = input('input album name:')
    if album_name == 'quit':
        break
    choice = input('\nWould you want to add album number (True/False)').lower()
    if choice == 'true':
        num = input("input album num:")
        if num == 'quit': break
    elif choice == 'quit': break
    
    print(f"\n{make_album(singer_name,album_name,num)}\n")