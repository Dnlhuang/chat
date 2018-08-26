
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:   #utf-8-sig 去掉記事本\ufeff編碼
        for line in f:
            lines.append(line.strip())
        return lines

def convert(lines):
    new = []
    person = None   #給person預設值
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue   #continue為了躲過new.append
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person:   #如果person有值（不等於None)
            new.append(person + ': ' + line)
    return new   #return就可以存檔
        
def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')


def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt', lines)



main()