import osmium
import json
import gc

class OSMHandler(osmium.SimpleHandler):
    def __init__(self, writer):
        super().__init__()
        self.writer = writer
        self.num = 0

    def node(self, n):
        if "name" not in n.tags:
            return

        item = {
            "id": "N" + str(n.id),
            "tags": {t.k: t.v for t in n.tags},
            'location': {
                "lat": n.location.lat,
                "lon": n.location.lon
            },
            "timestamp": int(n.timestamp.timestamp()),
            "uid": n.uid,
            "user": n.user,
            "user_is_anonymous": n.user_is_anonymous(),
            "deleted": n.deleted,
            "changeset": n.changeset,
            "version": n.version,
            "visible": n.visible
        }

        if self.num % 1000 == 0:
            print(self.num, item)
            gc.collect()
            
        self.num += 1
        
        self.writer.write(json.dumps(item, ensure_ascii=False) + "\n")
        
        del item

    def way(self, n):
        if "name" not in n.tags:
            return

        item = {
            "id": "W" + str(n.id),
            "tags": {t.k: t.v for t in n.tags},
            "timestamp": int(n.timestamp.timestamp()),
            "uid": n.uid,
            "user": n.user,
            "user_is_anonymous": n.user_is_anonymous(),
            "deleted": n.deleted,
            "changeset": n.changeset,
            "version": n.version,
            "visible": n.visible
        }

        if self.num % 1000 == 0:
            print(self.num, item)
            gc.collect()
            
        self.num += 1
        
        self.writer.write(json.dumps(item, ensure_ascii=False) + "\n")
        
        del item

    def relation(self, n):
        if "name" not in n.tags:
            return

        item = {
            "id": "R" + str(n.id),
            "tags": {t.k: t.v for t in n.tags},
            "timestamp": int(n.timestamp.timestamp()),
            "uid": n.uid,
            "user": n.user,
            "user_is_anonymous": n.user_is_anonymous(),
            "deleted": n.deleted,
            "changeset": n.changeset,
            "version": n.version,
            "visible": n.visible
        }

        if self.num % 1000 == 0:
            print(self.num, item)
            gc.collect()
            
        self.num += 1
        
        self.writer.write(json.dumps(item, ensure_ascii=False) + "\n")
        
        del item
        
if __name__ == "__main__":
    #http://download.geofabrik.de/asia/vietnam-latest.osm.pbf
    with open("vietnam-lastest.osm.jsonl", "a", encoding="utf8") as f:
        osm = OSMHandler(f)
        osm.apply_file("vietnam-latest.osm.pbf")