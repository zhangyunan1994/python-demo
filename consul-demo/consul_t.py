import unittest
import consul
import random


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_deregister(self):
        c = consul.Consul()
        return c.agent.service.deregister('python-user8384')

    def test_consul_register(self):
        c = consul.Consul()
        c.agent.service.register(name='python-user',
                                 service_id=f'python-user{random.randint(1000, 9999)}',
                                 address='192.168.1.7',
                                 port=8090,
                                 tags=['secure=false'],
                                 check={
                                     "DeregisterCriticalServiceAfter": "30s",
                                     "HTTP": "http://192.168.1.7:8090/hello",
                                     "Interval": "5s",
                                     "Timeout": "5s",
                                 }
                                )
        print(c.catalog.services())
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
