# coding:utf-8
from MySQLdb import connect
from settings import ProdConfig


class DB(object):
    def __init__(self,
                 username=ProdConfig.USER,
                 passwd=ProdConfig.PASSWD,
                 hostname=ProdConfig.HOST,
                 db=ProdConfig.DATABASE):
        self._con = connect(hostname, username, passwd, db)

    @staticmethod
    def Dict2Str(Dict):
        header = Dict.keys()
        # insert data must be include ''
        body = ['"' + str(Dict[key]) + '"' for key in header]
        return header, body

    def execute(self, cmd, get_all=True):
        with self._con as cur:
            cur.execute(cmd)
            if get_all:
                return cur.fetchall()
            else:
                return cur.fetchone()

    def insert(self, table, Dict):
        header, body = self.Dict2Str(Dict)
        with self._con as cur:
            cmd = "insert into {table} ({head}) VALUES ({val});".format(
                table=table,
                head=','.join(header),
                val=','.join(body)
            )
            cur.execute(cmd)

    def insert_all(self, table, Dict_list):
        cmd = "insert into {table} ({head}) VALUES ({val});"
        with self._con as cur:
            for each in Dict_list:
                header, body = self.Dict2Str(each)
                cur.execute(cmd.format(
                    table=table,
                    head=','.join(header),
                    val=','.join(body)
                ))

    def update(self, table, Dict, condDict):
        header, body = self.Dict2Str(Dict)
        updateList = []
        for head, val in zip(header, body):
            updateList.append('='.join([head, val]))
        with self._con as cur:
            cmd = "update {table} set {update} WHERE {key}='{value}';".format(
                table=table,
                update=','.join(updateList),
                key=condDict.keys()[0],
                value=condDict.values()[0]
            )
            cur.execute(cmd)

    def delete(self, table, condDict):
        with self._con as cur:
            cmd = "delete from {table} WHERE {key}='{value}';".format(
                table=table,
                key=condDict.keys()[0],
                value=condDict.values()[0]
            )
            cur.execute(cmd)


if __name__ == '__main__':
    db = DB()
    db.insert_all('haha', [{'NAME': 'chencheng'},
                           {'NAME': 'lxgui'},
                           {'NAME': 'liuhao'}])





