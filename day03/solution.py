class RucksackSolver:
    """Contains methods to fix messy rucksacks
    """

    def __init__(self, input_rucksacks):
        self.input_rucksacks = input_rucksacks
        self.rucksacks = []
        for r in input_rucksacks:
            l = len(r)
            comp = (r[:int(l/2)], r[int(l/2):])
            self.rucksacks.append(comp)
        self.prio = 0
        for r in self.rucksacks:
            self.prio += self.find_wrong_item_prio(r)

        self.groups = []
        self.badge_prio = 0
        for r in range(0, len(self.input_rucksacks), 3):
            self.badge_prio += self.find_badge_prio(self.input_rucksacks[r:r + 3])

        
    def find_wrong_item_prio(self, r):
        """Finds wrongly sorted item by checking which item is in both compartments.
        Assigns a prio: a-z == 1-26, A-Z == 27-52
        """
        wrong = None
        for item in r[0]:
            if r[1].find(item) != -1:
                wrong = item
                break
        return(self.get_prio(wrong))

    def find_badge_prio(self, rucksacks):
        """Finds wrongly sorted item by checking which item is in 3 consecutive backpacks
        """

        for item in rucksacks[0]:
            if rucksacks[1].find(item) != -1:
                if rucksacks[2].find(item) != -1:
                    badge = item
        return(self.get_prio(badge))


    def get_prio(self, item):
        """We will compute the prio based on the ascii rank of the char
        """
        ascii_rank = ord(item)
        if ascii_rank >= 97:
            prio = ascii_rank - 96
        else:
            prio = ascii_rank - 64 + 26
        return prio




with open("input.txt", "r") as input:
    rucksacks = input.readlines()
    rucksacks = [rucksack.strip('\n') for rucksack in rucksacks]
    rucksacksolver = RucksackSolver(rucksacks)
    print(rucksacksolver.prio)
    print(rucksacksolver.badge_prio)

