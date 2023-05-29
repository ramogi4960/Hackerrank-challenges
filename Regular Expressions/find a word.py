import re
"""
10
independent(rented rented.the aggressive-rented-grand agreement)rented-star altogetherrented rented(consequence politician_rented pile(rented alarm(rented movie.rented_visible
rented.february rentedson rented'slight ceremony'rented serve-rented behalf_rented skirt'rented rented,broken cough-rented stiff,rented-chop
freeze.rented(angrily rented)beard rentedtax proposal_rentedmoment suddenly'rented-occupy rented,neatly tablet)rentedfly wonderfulrented-festival coldly.rented'candidate rented.department
purchaserented imagine'rented invest.rented rented.counter rented,hero rented'innocent coat,rented.health dealrented-accurate building)rented,unexpected rented-unsuccessful
rented.new way-rented)language piece(rented qualification(rented-investment preserverentedsweat untidyrentedcriterion irritated(rented age-rented base_rented_expectation prisoner)rented
fit(rented guardrented ours)rented)personally rented'unfortunate cough.rented rented,effort ending(rented'yellow slow)rented-satisfied upside)rented,model artificially.rented
university.rented throughout-rented rented.school criterion,rented)look such'rented rentedabsolutely honest-rented salad_rented sliprentedrightly rented_shall
rented)walk rented'council cow'rented.garbage lock.rented,vote weight)rented salt-rented rented)retire programrentedfly yellow'rented rented(nut
bubblerented secret'rented electronic(rented writer'rented-can introduction'rented(old rented'citizen rented)personality rented(understanding rentedsoldier map-rented.please
improvement.rented rented-chip rented.easy sew'rented government(rented riding(rented rented'complicate keep)rented rented-damp silence(rented-succeed
1
rented
"""
sentences = [input() for _ in range(int(input()))]
words = [input() for _ in range(int(input()))]
for item in words:
    count = 0
    pattern = rf"\b{item}\b"
    for i in sentences:
        count += len(re.findall(pattern, i))
    print(count)
