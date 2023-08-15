staffs_list = []
vips_list = []
txt_file_way = ""


try:
    with open("settings.txt", 'r') as file:
        for v in file:
            v = v.replace("\n", "")
            data = v.split(",")
            if data[0] == "player_list_file_way":
                txt_file_way = data[1]
            elif data[0] == "staffs":
                count = 0
                for g in data:
                    count +=1
                    if count >=2:
                        staffs_list.append(g)
            elif data[0] == "vips":
                count= 0
                for g in data:
                    count +=1
                    if count >=2:
                        vips_list.append(g)
except FileNotFoundError:
    print(f"Dosya bulunamadı: settings.txt")
except IOError as e:
    print(f"Dosya okuma hatası: {e}")



def getPlayerCount():
    try:
        with open(txt_file_way, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Dosya bulunamadı: {txt_file_way}")
        return False
    except IOError as e:
        print(f"Dosya okuma hatası: {e}")
        return False


def getPlayerList():
    players = getPlayerCount()
    if players:
        try:
            players = players.split("\n")
            #sent values
            player_count = 0
            staffs = ""
            vips = ""
            player_list = ""
            for v in players:
                staff_state = False
                vip_state = False
                v = v.replace("\n", "")
                player_data = v.split(",")
                print(player_data)
                for a in staffs_list:
                    if a == player_data[1]:
                        staff_state = True
                for a in vips_list:
                    if a == player_data[2]:
                        vip_state = True
                if staff_state:
                    staffs += player_data[0]+"\n"
                elif vip_state:
                    vips += player_data[0]+"\n"
                else:
                    player_list += player_data[0]+"\n"
                player_count +=1
            return player_count,staffs,vips,player_list
        except:
            return 0,"","",""
    else:
        return 0,"","",""


