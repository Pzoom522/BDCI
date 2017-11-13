def is_chinese(uchar):
    if uchar >= '\u4e00' and uchar<='\u9fff':
        return True
    else:
        return False

#entity cleanup: modify / delete not-so-likely entities
input = open("input.file",mode="r",encoding="utf-8")
output = open("output.file",mode="w",encoding="utf-8")
while True:
    line = input.readline()
    if not line:
        break
    entities = line.split()
    entities = list(set(entities))  # now unique

    #entities not starting with Chinese
    for i in range (0, len(entities)):
        e = entities[i]
        if not is_chinese(e[0]):
            while not is_chinese(e[0]):
                if len(e)>1:
                    e = e[1:]
            if(len(e) == 1):
                entities[i] = ' '
            else:
                entities[i] = e
    for e in entities:
        if (e == ' '):
            entities.remove(e)

    entities = list(set(entities))
    
    #entities ending with '网' and '报' - remove from list
    for entity in entities:
        if entity.endswith('网') or entity.endswith('报'):
            entities.remove(entity)

    entities = list(set(entities))

    #remove entities sticking together
    exception_length = 10 # max length to find exception pattern

    l = len(entities)
    i = 0
    while i < l:
        e = entities[i]
        index = e.find('有限公司')
        if index != -1 and index + 4 != len(e):
            exception_index = e.find('分公司')
            if exception_index != -1 and exception_index - index < exception_length:
                i = i + 1
                continue
            entities[i] = e[:index + 4]
            entities.append(e[index + 4:])
            l = l + 1
        i = i + 1

    l = len(entities)
    i = 0
    while i < l:
        e = entities[i]
        index = e.find('分公司')
        if index != -1 and index + 3 != len(e):
            entities[i] = e[:index + 3]
            entities.append(e[index + 3:])
            l = l + 1
        i = i + 1

    entities = list(set(entities))
    
    l = len(entities)
    i = 0
    while i < l:
        e = entities[i]
        index = e.find('超市')
        if index != -1 and index + 2 != len(e):
            exception_index = e.find('有限公司')
            exception_index = e.find('店')
            if exception_index != -1 and exception_index - index < exception_length:
                i = i + 1
                continue
            entities[i] = e[:index + 2]
            entities.append(e[index + 2:])
            l = l + 1
        i = i + 1
    
    entities = list(set(entities))

    l = len(entities)
    i = 0
    while i < l:
        e = entities[i]
        index = e.find('管理局')
        if index != -1 and index + 3 != len(e):
            exception_index = e.find('分局')
            if exception_index != -1 and exception_index - index < exception_length:
                i = i + 1
                continue
            entities[i] = e[:index + 3]
            entities.append(e[index + 3:])
            l = l + 1
        i = i + 1

    l = len(entities)
    i = 0
    while i < l:
        e = entities[i]
        index = e.find('分局')
        if index != -1 and index + 2 != len(e):
            entities[i] = e[:index + 2]
            entities.append(e[index + 2:])
            l = l + 1
        i = i + 1

    entities = list(set(entities))

    l = len(entities)
    i = 0
    while i < l:
        e = entities[i]
        index = e.find('食品厂')
        if index != -1 and index + 3 != len(e):
            exception_index = e.find('分厂')
            if exception_index != -1 and exception_index - index < exception_length:
                i = i + 1
                continue
            entities[i] = e[:index + 3]
            entities.append(e[index + 3:])
            l = l + 1
        i = i + 1

    l = len(entities)
    i = 0
    while i < l:
        e = entities[i]
        index = e.find('分厂')
        if index != -1 and index + 2 != len(e):
            entities[i] = e[:index + 2]
            entities.append(e[index + 2:])
            l = l + 1
        i = i + 1

    entities = list(set(entities))

    l = len(entities)
    i = 0
    while i < l:
        e = entities[i]
        index = e.find('经营部')
        if index != -1 and index + 3 != len(e):
            entities[i] = e[:index + 3]
            entities.append(e[index + 3:])
            l = l + 1
        i = i + 1

    entities = list(set(entities))

    l = len(entities)
    i = 0
    while i < l:
        e = entities[i]
        index = e.find('加工厂')
        if index != -1 and index + 3 != len(e):
            entities[i] = e[:index + 3]
            entities.append(e[index + 3:])
            l = l + 1
        i = i + 1

    entities = list(set(entities))

    l = len(entities)
    i = 0
    while i < l:
        e = entities[i]
        index = e.find('研究院')
        if index != -1 and index + 3 != len(e):
            entities[i] = e[:index + 3]
            entities.append(e[index + 3:])
            l = l + 1
        i = i + 1

    entities = list(set(entities))

    l = len(entities)
    i = 0
    while i < l:
        e = entities[i]
        index = e.find('批发部')
        if index != -1 and index + 3 != len(e):
            entities[i] = e[:index + 3]
            entities.append(e[index + 3:])
            l = l + 1
        i = i + 1

    entities = list(set(entities))

    l = len(entities)
    i = 0
    while i < l:
        e = entities[i]
        index = e.find('加油站')
        if index != -1 and index + 3 != len(e):
            exception_index = e.find('有限公司')
            if exception_index != -1 and exception_index - index < exception_length:
                i = i + 1
                continue
            entities[i] = e[:index + 3]
            entities.append(e[index + 3:])
            l = l + 1
        i = i + 1

    entities = list(set(entities))


    #write to file
    for entity in entities:
        output.write(entity + ' ')
    output.write('\n')