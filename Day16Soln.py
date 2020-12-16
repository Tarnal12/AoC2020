class Ticket():
    def __init__(self, ticket_string: str):
        self.fields = [int(field) for field in ticket_string.split(',')]

class TicketRule():
    def __init__(self, rule_string: str):
        # departure location: 41-525 or 538-968
        (field_name, field_values) = rule_string.split(': ')
        self.field_name = field_name
        self.rule = []
        for value_pair in field_values.split(' or '):
            as_ints = tuple(map(int, value_pair.split('-')))
            self.rule.append(as_ints)

    def is_valid(self, value: int) -> bool:
        for pair in self.rule:
            if value >= pair[0] and value <= pair[1]:
                return True
        return False

    def __repr__(self):
        return f'<TicketRule ({self.field_name}: {self.rule})'


def main():
    with open("Day16Input.txt", "r") as f:
        blocks = f.read().split('\n\n')

    ticket_rules = []
    for rule in blocks[0].split('\n'):
        ticket_rules.append(TicketRule(rule))

    my_ticket = Ticket(blocks[1].split('\n')[1])

    tickets = []
    for ticket in blocks[2].split('\n')[1:]:
        tickets.append(Ticket(ticket))

    # Check every value against every rule to see if it's even potentially valid
    ticket_scan_err_rate = 0
    tickets_to_remove = []
    for ticket in tickets:
        for field in ticket.fields:
            matches_any_rule = False
            for rule in ticket_rules:
                matches_any_rule = matches_any_rule or rule.is_valid(field)
            if not matches_any_rule:
                ticket_scan_err_rate += field
                tickets_to_remove.append(ticket)
    print(ticket_scan_err_rate)

    # Strip invalid tickets
    for ticket in tickets_to_remove:
        tickets.remove(ticket)

    possible_indices = {}
    for rule in ticket_rules:
        possible_indices[rule] = [i for i in range(len(ticket_rules))]
        for ticket in tickets:
            tickets_possible_indices = [i for i in possible_indices[rule] if rule.is_valid(ticket.fields[i])]
            possible_indices[rule] = list(set(possible_indices[rule]).intersection(tickets_possible_indices))
        #print(f"{rule} could be any of these: {tickets_possible_indices}")

    certain_indices = {}
    while len(certain_indices) < len(ticket_rules):
        for rule in possible_indices:
            if len(possible_indices[rule]) == 1:
                certain_indices[rule] = possible_indices[rule][0]

            for confirmed_rule in certain_indices:
                taken_index = certain_indices[confirmed_rule]
                this_rules_indices = possible_indices[rule]
                if taken_index in this_rules_indices:
                    possible_indices[rule].remove(taken_index)
    
    product = 1
    for rule in certain_indices:
        if rule.field_name[:9] == 'departure':
            product *= my_ticket.fields[certain_indices[rule]]
    print(product)



if __name__ == "__main__":
    main()
