players = {

}

------------------------------------
--Write to file
------------------------------------
function writeToFile(fileName, content)
    local file = fileCreate(fileName)
    if file then
        fileWrite(file, content)
        fileClose(file)
        return true
    else
        return false
    end
end


------------------------------------
--Start Discord Status
------------------------------------
function startFunc()
    local plrs = getElementsByType("player")
    local text = tostring(#plrs).."\n"
    for k,v in ipairs(plrs) do
        local player_name = string.gsub(getPlayerName(v), "#%x%x%x%x%x%x", "") 
        local acl = getElementData(v,"ata:acl_name") or ""
        text = text..player_name..","..acl.."\n"
        players[v] = {name = player_name,acl = acl}
    end
    writeToFile("player_count.txt",text)
end

addEventHandler("onResourceStart",resourceRoot,startFunc)

--------------------------------------------------
--Write text
--------------------------------------------------
function writeText()
    local text = ""
    local count = 0
    local text =""
    for k,v in pairs(players) do 
        text = text..v.name..","..v.acl.."\n"
        count = count +1
    end
    text = tostring(count).."\n"..text
    writeToFile("player_count.txt",text)
end

--------------------------------------------------
--On player join
--------------------------------------------------
function playerJoin()
    setTimer(function(plr)
        local player_name = string.gsub(getPlayerName(plr), "#%x%x%x%x%x%x", "") 
        local acl = getElementData(plr,"ata:acl_name") or ""
        players[plr] = {name = player_name,acl=acl}
        writeText()
    end,1000,1,source)
end
addEventHandler("onPlayerLogin",root,playerJoin)


--------------------------------------------------
--On player join
--------------------------------------------------
function playerQuit()
    players[source] = nil
    writeText()
    outputConsole(#players)
end
addEventHandler("onPlayerQuit",root,playerQuit)



