def ctd2svp(ctdpath, svppath):
  with open(ctdpath, 'r') as f:
    output = []
    line = f.readline()
    while line:
      line = line.split('\t').replace('\n', '')
      output.append([line[3], line[4])
      line = f.readline()
  with open(svppath, 'w') as f:
    f.write('\n')
    f.write('\n'.join(['\t'.join(line) for line in output])

if __name__ == '__main__':
  ctd2svp('../data/VehicleCTD.txt', '../data/svp.txt')
