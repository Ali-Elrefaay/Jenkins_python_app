from flask import Flask, render_template
import subprocess

app = Flask(__name__)

def get_protocol_port_info():
    # Run the netstat command
    netstat_output = subprocess.check_output(['netstat', '-tln']).decode('utf-8')

    # Split the output by lines and remove the header
    netstat_lines = netstat_output.strip().split('\n')[2:]

    # Initialize a list to store protocol and port tuples
    protocol_port_list = []

    # Iterate through each line of the output
    for line in netstat_lines:
        # Split the line by whitespace
        parts = line.split()
        # Extract protocol and port number
        protocol = parts[0]
        local_address = parts[3]
        port = local_address.split(':')[-1]
        # Append protocol and port number to the list
        protocol_port_list.append((protocol, port))

    return protocol_port_list

@app.route('/')
def index():
    protocol_port_list = get_protocol_port_info()
    return render_template('index.html', protocol_port_list=protocol_port_list)

if __name__ == '__main__':
    app.run(debug=True)
