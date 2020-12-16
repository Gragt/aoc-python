"""Puzzle 04 solutions."""

import re

import helpers


def parser(data):
    """Parse data into a list of dictionaries."""
    regex = re.compile(r"([a-z]{3}):([\w#]*)")
    parsed_data = []
    wip = {}
    for line in data:
        if not line:
            parsed_data.append(wip)
            wip = {}
        else:
            wip.update(regex.findall(line))
    parsed_data.append(wip)
    return tuple(parsed_data)


def check_validity(passport):
    """Check if a passport is valid."""
    return len(passport) == 8 or len(passport) == 7 and "cid" not in passport


def check_validity2(passport):
    """Check password validity in details."""

    def check_byr(byr):
        """Check byr validity."""
        return byr >= 1920 and byr <= 2002

    def check_iyr(iyr):
        """Check iyr validity."""
        return iyr >= 2010 and iyr <= 2020

    def check_eyr(eyr):
        """Check eyr validity."""
        return eyr >= 2020 and eyr <= 2030

    def check_hgt(hgt):
        """Check hgt validity."""
        regex = re.compile(r"^(\d+)(cm|in)$")
        if not bool(regex.match(hgt)):
            return False
        height, unit = regex.match(hgt).groups()
        if unit == "cm":
            return int(height) >= 150 and int(height) <= 193
        elif unit == "in":
            return int(height) >= 59 and int(height) <= 76

    def check_hcl(hcl):
        """Check hcl validity."""
        regex = re.compile(r"^#[0-9a-f]{6}$")
        return bool(regex.match(hcl))

    def check_ecl(ecl):
        """Check ecl validity."""
        valid_ecl = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
        return ecl in valid_ecl

    def check_pid(pid):
        """Check pid validity."""
        regex = re.compile(r"^\d{9}$")
        return bool(regex.match(pid))

    if not check_validity(passport):
        return False

    return (
        check_byr(int(passport.get("byr")))
        and check_iyr(int(passport.get("iyr")))
        and check_eyr(int(passport.get("eyr")))
        and check_hgt(passport.get("hgt"))
        and check_hcl(passport.get("hcl"))
        and check_ecl(passport.get("ecl"))
        and check_pid(passport.get("pid"))
    )


def count_valid_passports(passports):
    """Count the number of valid passports."""
    return sum(check_validity(passport) for passport in passports)


def count_valid_passports2(passports):
    """Count the number of valid passports in detail."""
    return sum(check_validity2(passport) for passport in passports)


data = parser(helpers.linereader("04.txt"))
print(count_valid_passports(data))
print(count_valid_passports2(data))
