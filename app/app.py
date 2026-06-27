from http.server import BaseHTTPRequestHandler, HTTPServer
import psycopg2
import time
import json

time.sleep(5)

class Handler(BaseHTTPRequestHandler):
   def do_GET(self):

      if self.path != "/taches":
          self.send_response(404)
          self.end_headers()
          self.wfile.write(b"Page non trouvee")
          return

      conn = psycopg2.connect(
          host="db",
          database="devopsdb",
          user="sara",
          password="motdepasse123"
      )

      cursor = conn.cursor()

      cursor.execute("SELECT * FROM taches ORDER BY id;")

      taches = cursor.fetchall()

      resultat = []

      for tache in taches:
          resultat.append({
              "id": tache[0],
              "nom": tache[1]
          })

      self.send_response(200)
      self.send_header("Content-type", "application/json")
      self.end_headers()
      self.wfile.write(json.dumps(resultat).encode())

      cursor.close()
      conn.close()

   def do_POST(self):

      print("POST reçu")

      content_length = int(self.headers['Content-Length'])
      body = self.rfile.read(content_length)

      data = json.loads(body.decode())

      nom = data["nom"]

      conn = psycopg2.connect(
          host="db",
          database="devopsdb",
          user="sara",
          password="motdepasse123"
      )

      cursor = conn.cursor()

      cursor.execute(
          "INSERT INTO taches (nom) VALUES (%s)",
          (nom,)
      )

      conn.commit()

      cursor.close()
      conn.close()

      self.send_response(201)
      self.send_header("Content-type", "application/json")
      self.end_headers()

      self.wfile.write(json.dumps({"message": "tache ajoutee"}).encode())

   def do_PUT(self):

      id_tache = self.path.split("/")[-1]

      content_length = int(self.headers["Content-Length"])

      body = self.rfile.read(content_length)

      data = json.loads(body.decode())

      nouveau_nom = data["nom"]

      conn = psycopg2.connect(
          host="db",
          database="devopsdb",
          user="sara",
          password="motdepasse123"
      )

      cursor = conn.cursor()

      cursor.execute(
          "UPDATE taches SET nom = %s WHERE id = %s",
          (nouveau_nom, id_tache)
      )

      conn.commit()

      cursor.close()
      conn.close()

      print("ID :", id_tache)
      print("Nouveau nom :", nouveau_nom)

      self.send_response(200)
      self.send_header("Content-type", "application/json")
      self.end_headers()

      self.wfile.write(
          json.dumps(
              {"message": "PUT reçu"}
          ).encode()
      )

   def do_DELETE(self):

      id_tache = self.path.split("/")[-1]

      conn = psycopg2.connect(
          host="db",
          database="devopsdb",
          user="sara",
          password="motdepasse123"
      )

      cursor = conn.cursor()

      cursor.execute(
          "DELETE FROM taches WHERE id = %s",
          (id_tache,)
      )

      conn.commit()

      cursor.close()
      conn.close()

      self.send_response(200)
      self.send_header("Content-type", "application/json")
      self.end_headers()

      self.wfile.write(
          json.dumps({"message": "tache supprimee"}).encode()
      )

server = HTTPServer(("0.0.0.0", 8000), Handler)

print("API démarrée sur le port 8000")

server.serve_forever()
