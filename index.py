import DBService 

DBService.DBConnect("UserData.db", "User")
DBService.checkTableReady()

#DBService.insert("test", "2000-01-01")

#DBService.update(2, "test2", "2001-01-01")

#DBService.delete(2)

#selectResult = DBService.select_By_ID(3)
selectResult = DBService.select_All()
print(selectResult)

DBService.DBClose()
