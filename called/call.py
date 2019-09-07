#!/usr/bin/python

def main():
    f = open("/Users/victorcamargo/Desktop/metrics-exporter/templates/textfile.txt", "w+")
    f.write("# Teste teste teste \n# Teste teste teste \nchave valor")
    f.close()

if __name__ == "__main__":
    main()
