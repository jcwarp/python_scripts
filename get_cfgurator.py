from pymongo import MongoClient
import argparse
import json
import yaml
import print_instance

def db_connect():
  # Create and validate connection
  # Creating a pymongo client
  client = MongoClient('localhost', 27017)
  # Getting the database instance
  db = client['cvClusterManager']
  return db
 
def get_collection(db):
  # Getting the DB Collection
  collection = db['clusters']
  return collection
 
def get_instance_doc(instance,coll):
  for document in coll.find( instance).sort('clusterId'):
    return document

# Main #
if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="Injest json config for instance, and output yaml.")
  parser.add_argument("-c", "--customer", default='all', help='instance name of customer')
  parser.add_argument("-d", "--dictionary", action=argparse.BooleanOptionalAction, default=False, help='output in basic dictionary format')
  parser.add_argument("-ls", "--list", action=argparse.BooleanOptionalAction, default=False, help='list databases in Mongo')
  args = parser.parse_args()

  db = db_connect()
  coll = get_collection( db )

  if coll is None:
    print("Collection is empty")
  else:
    if args.list:
      # List databases
      print("List of databases: ")
      print(client.list_database_names())
      print("Records of the collection: ")
      # Get list of DM instances in Mongo
      for instance in coll.find({},{'clusterId':1, '_id':0}).sort('clusterId'):
        print(instance)
 
    else:
      # One instance or all
      if args.customer == 'all':
        # Loop through list of instances sorted by clusterID
        for instance in coll.find({},{'clusterId':1, '_id':0}).sort('clusterId'):
          # Populate DM Instance dict
          get_instance_doc(instance)
      else:
        instance={'clusterId': args.customer}
        # Populate DM Instance dict
        config=get_instance_doc( instance, coll )
        #print('Record of the collection for %s: ' % instance["clusterId"])
        if args.dictionary:
          print( config)
        else:
          print(yaml.dump( config, default_flow_style=False ))
          print_instance.print_yaml( config)

        #REVERSED_CFG = dict(map(reversed, config))
        #print(yaml.dump( REVERSED_CFG, default_flow_style=False ))

        # print("DB Username: %s" % yaml.dump(config['properties']['db_username'], default_flow_style=False, default_style='"'))
 
        # j = 0
        # for i in doc['nodes']:
        #   print( 'Node index ' + str(j) + ' Node ID: ' + i['nodeId'])
        #   j +=1
 
        # print("%s DB Nodes: " % args.customer)
        # print(yaml.dump(doc['properties']['db_username'], default_flow_style=False))





  # Translate dict to hiera data variables

  # Output instance_names_v2 eyaml

# Done
