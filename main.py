from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
import subprocess

class PingMasterApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10)
        self.report = Label(text="Initializing Multi-IP Ping Analysis...\n", 
                           size_hint_y=None, halign='left', valign='top')
        self.report.bind(texture_size=self.report.setter('size'))
        
        scroll = ScrollView()
        scroll.add_widget(self.report)
        layout.add_widget(scroll)
        
        # Original Requirement: Detailed 3 pings [cite: 2025-12-14]
        self.run_ping_test()
        return layout

    def run_ping_test(self):
        target_ips = ["8.8.8.8", "1.1.1.1"] # Your Multi-IP list [cite: 2025-12-14]
        summary = "\nFINAL STATUS SUMMARY\n" + "="*30 + "\n"
        
        for ip in target_ips:
            try:
                # Performing 3 detailed pings [cite: 2025-12-14]
                output = subprocess.check_output(['ping', '-c', '3', ip], stderr=subprocess.STDOUT).decode()
                status = "OK" [cite: 2025-12-14]
            except:
                status = "NOT OK" [cite: 2025-12-14]
            
            summary += f"IP: {ip} | Status: {status}\n"
        
        self.report.text += summary

if __name__ == '__main__':
    PingMasterApp().run()
