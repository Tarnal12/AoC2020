import re


class Passport():
    def __init__(self, data: str):
        data = data.replace('\n', ' ')
        self.data_map = {}
        for data_item in data.split(' '):
            (data_key, data_value) = data_item.split(':')
            self.data_map[data_key] = data_value

        #print(f"{data} is valid? {self.is_valid()}")
    
    def is_valid(self):
        try:
            if int(self.data_map['byr']) < 1920 or int(self.data_map['byr']) > 2002:
                return False
                
            if int(self.data_map['iyr']) < 2010 or int(self.data_map['iyr']) > 2020:
                return False
                
            if int(self.data_map['eyr']) < 2020 or int(self.data_map['eyr']) > 2030:
                return False

            height_units = self.data_map['hgt'][-2:]
            height_val = int(self.data_map['hgt'][:-2])
            if (
                height_units not in ('cm', 'in') or
                (height_units == 'cm' and (height_val < 150 or height_val > 193)) or
                (height_units == 'in' and (height_val < 59 or height_val > 76))
            ):
                return False

            hair_color_re = re.compile("^#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]$")
            if not hair_color_re.match(self.data_map['hcl']):
                return False

            if self.data_map['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                return False

            if len(self.data_map['pid']) != 9 or not self.data_map['pid'].isnumeric():
                return False

            return (
                'byr' in self.data_map and
                'iyr' in self.data_map and
                'eyr' in self.data_map and
                'hgt' in self.data_map and
                'hcl' in self.data_map and
                'ecl' in self.data_map and
                'pid' in self.data_map
            )
        except Exception as e:
            return False


if __name__ == "__main__":
    with open("Day4Input.txt", "r") as f:
        contents = f.read()
        documents = [block for block in contents.split('\n\n')]

    valid_count = 0
    for document in documents:
        passport = Passport(document)
        valid_count += passport.is_valid()

    print(valid_count)
