import subprocess

class utility:

    def selectNetwork(self,selectednetwork):
        networks = subprocess.check_output(['netsh', 'wlan', 'show', 'networks']).decode()

        ssid_list = []
        for line in networks.split('\n'):
                if 'SSID' in line:
                    ssid_list.append(line.split(':')[3].strip())
                print(ssid_list)
                selected_network = input(selectednetwork)
                subprocess.run(['netsh', 'wlan', 'connect', 'name=' + selected_network])
                subprocess.run(['netsh', 'interface', 'set', 'interface', selected_network, 'admin=enable'])

        return subprocess.check_output