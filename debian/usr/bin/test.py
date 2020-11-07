import unittest
import set

# TestCase를 작성
class CustomTests(unittest.TestCase):

    def test_runs(self):
        set.set_alarm()
        set.set_password()
        set.set_update()
        set.set_ufw()
        set.set_backup()

# unittest를 실행
if __name__ == '__main__':
    unittest.main()