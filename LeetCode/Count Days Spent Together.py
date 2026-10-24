
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        alice_arrive_month = int(arriveAlice[:2])
        alice_leave_month = int(leaveAlice[:2])
        alice_arrive_day = int(arriveAlice[3:])
        alice_leave_day = int(leaveAlice[3:])

        bob_arrive_month = int(arriveBob[:2])
        bob_leave_month = int(leaveBob[:2])
        bob_arrive_day = int(arriveBob[3:])
        bob_leave_day = int(leaveBob[3:])

        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        alice_arrive = alice_arrive_day
        alice_leave = alice_leave_day
        bob_arrive = bob_arrive_day
        bob_leave = bob_leave_day

        for i in range(alice_arrive_month - 1):
            alice_arrive += months[i]

        for i in range(alice_leave_month - 1):
            alice_leave += months[i]

        for i in range(bob_arrive_month - 1):
            bob_arrive += months[i]

        for i in range(bob_leave_month - 1):
            bob_leave += months[i]

        start = max(alice_arrive, bob_arrive)
        end = min(alice_leave, bob_leave)

        return max(0, end - start + 1)
