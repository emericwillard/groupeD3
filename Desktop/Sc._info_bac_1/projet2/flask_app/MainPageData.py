import sqlite3
conn = sqlite3.connect('inginious.sqlite')

cursor = conn.cursor()

def mainPage(course):
    #Calcul le nombre de soumissions par jour pour un cours
    def submissions_PerDay():
        l=[]
        d=[]
        c=[]
        date=[]
        for row in cursor.execute("SELECT submitted_on FROM submissions WHERE course LIKE \'"+str(course)+"\'"):
            l.append((row[0][:10]))
        l.sort()
        for i in range(len(l)):
            try:
                if l[i]==l[i+1]:
                    d.append(l[i])
                else:
                    d.append(l[i])
                    date.append(l[i])
                    c.append(d)
                    d = []
            except IndexError:
                d.append(l[i])
                date.append(l[i])
                c.append(d)

        avg_day=[]
        for i in c:
            avg_day.append(len(i))
        return(avg_day, date)

    #Calcule l'exercices le plus soumis du cours
    def hardest_ex():
        l=[]
        c=[]
        for row in cursor.execute("SELECT task, tried FROM user_tasks WHERE course like \'"+str(course)+"\'"):
            l.append((row[0], row[1]))
        l = sorted(l)
        sum = 0
        for i in range(len(l)):
            try:
                if l[i][0] == l[i+1][0]:
                    sum += l[i][1]
                else:
                    sum += l[i][1]
                    c.append([sum, l[i][0]])
                    sum = 0
            except IndexError:
                sum+=l[i][1]
                c.append([sum, l[i][0]])
        c = sorted(c, reverse=True)[:10]
        tried=[]
        task=[]   
        for x, y in c:
            tried.append(x)
            task.append(y)
        return(tried, task)

    #Calcul l'exercie le moins soumis
    def easiest_ex():
        l=[]
        c=[]
        for row in cursor.execute("SELECT task, tried FROM user_tasks WHERE course like \'"+str(course)+"\'"):
            l.append((row[0], row[1]))
        l = sorted(l)
        sum = 0
        for i in range(len(l)):
            try:
                if l[i][0] == l[i+1][0]:
                    sum += l[i][1]
                else:
                    sum += l[i][1]
                    c.append([sum, l[i][0]])
                    sum = 0
            except IndexError:
                sum+=l[i][1]
                c.append([sum, l[i][0]])
        c = sorted(c)
        a = 0
        for i in range(len(c)):
            if a == 10:
                break
            elif c[i][0]>0:
                s = []
                for j in range(i, len(c)):
                    a += 1
                    s.append(c[j])
                    if a == 10:
                        break
        tried=[]
        task=[]
        for x, y in s:
            tried.append(x)
            task.append(y)
        return(tried, task)
    return(submissions_PerDay(), hardest_ex(), easiest_ex())

conn.close()

