import requests
import json
import sys
import threading
import time

def get_ticket():
        url = "https://10.0.0.22:8006/api2/extjs/access/ticket"
        payload = {
                "username":"root",
                "password":"rootroot",
                "realm":"ovp"
        }

        r = requests.post(url,data=payload,verify=False)
        data = r.json()['data']
        ticket = data["ticket"]
        token = data["CSRFPreventionToken"]
        return ticket,token


def change_ip(vm_id,ip,headers,cookies):
        try:
                url = "https://10.0.0.22:8006/api2/extjs/nodes/OVP/qemu/%s/config" % vm_id
                r = requests.get(url,headers=headers,cookies=cookies,verify=False,timeout=5)
                digest = r.json()['data']['digest']

                payload = {
                        "delete":"dhcp",
                        "ip": ip,
                        "netmask":"255.255.252.0",
                        "gateway":"10.0.0.1",
                        "digist":digest
                }

                r = requests.put(url, headers=headers,cookies=cookies,verify=False,timeout=5,data=payload)
                print r.text

        except Exception,e:
                print e


def stop_vm(vm_id,headers,cookies):
        url = "https://192.168.18.100:8006/api2/extjs/nodes/OVP/qemu/%s/status/stop" % vm_id
        r = requests.post(url, headers=headers,cookies=cookies,verify=False,timeout=5)
        print r.text


def get_all_vms(headers,cookies):
        try:
                url = "https://10.0.0.22:8006/api2/json/cluster/resources"
                payload = {"type":"vm"}
                r = requests.get(url,headers=headers,cookies=cookies,verify=False,timeout=9,params=payload)
                return r.json()['data']

       except Exception,e:
                print e


if __name__ == '__main__':

        ticket,token = get_ticket()
        cookies = {
                "OVPAuthCookie":ticket
        }
        headers = {
                "CSRFPreventionToken":token
        }

        for vm in get_all_vms(headers,cookies):
                print vm



