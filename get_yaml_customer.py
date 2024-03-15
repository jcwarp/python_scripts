import sys
import argparse
import yaml
import align_yaml

def init_argparse() -> argparse.ArgumentParser:
  parser = argparse.ArgumentParser(
    usage="%(prog)s [OPTION] [FILE]...",
    description="Print list of yaml keys defined in hiera file, by customer"
  )
  parser.add_argument("-f", "--file", nargs='*', default='~/src/puppet/data/cluster/dm-stg-east1.eyaml', help='path to hiera data file')
  parser.add_argument("-c", "--customer", nargs='*', default='all', help='instance name of customer')
  parser.add_argument("-j", "--json", action=argparse.BooleanOptionalAction)
  parser.add_argument("-d", "--dictionary", action=argparse.BooleanOptionalAction)
  return parser

def open_hierafile( file ):
  yaml.prefix_colon = ' '
  yaml.top_level_colon_align = True
  yaml.indent = 2

  with open( file ) as file:
    hierafile = yaml.safe_load( file )
  return hierafile

class IndentDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(IndentDumper, self).increase_indent(flow, False)

#########################
# MAIN
#########################
def main() -> None:
  parser = init_argparse()
  args = parser.parse_args()

  for file in args.file:
    try:
      customer = args.customer
      hierafile = open_hierafile( file )
    except (FileNotFoundError, IsADirectoryError) as err:
      print(f"{sys.argv[0]}: {file}: {err.strerror}", file=sys.stderr)

  # Extract a subsection of the YAML data
  print( customer )
  subsection = hierafile['dm::acs_instance_names_v2'][args.customer[0]]
  if args.json:
    # Output json
    import print_config
    print_config.print_config(subsection, args.customer[0])
  elif args.dictionary:
    import make_config
    make_config.create_cfg(subsection, args.customer[0])
  else:
    subsect_text=yaml.dump(subsection, Dumper=IndentDumper)
    aligned_text=align_yaml.align_yaml(subsect_text, aligned_colons=True)
    print(aligned_text)

if __name__ == '__main__':
   main()
