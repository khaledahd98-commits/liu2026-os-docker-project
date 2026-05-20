from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Preformatted
from reportlab.lib.units import cm

pdf_path = '/mnt/data/liu2026_os_docker_project/docs/LIU2026_Report.pdf'
doc = SimpleDocTemplate(pdf_path, pagesize=A4, rightMargin=1.5*cm, leftMargin=1.5*cm, topMargin=1.5*cm, bottomMargin=1.5*cm)
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Title2', parent=styles['Title'], fontSize=20, leading=24, spaceAfter=12))
styles.add(ParagraphStyle(name='H1x', parent=styles['Heading1'], fontSize=16, leading=20, textColor=colors.HexColor('#1f4e79')))
styles.add(ParagraphStyle(name='H2x', parent=styles['Heading2'], fontSize=13, leading=16, textColor=colors.HexColor('#2f5597')))
styles.add(ParagraphStyle(name='Bodyx', parent=styles['BodyText'], fontSize=10.5, leading=14, spaceAfter=7))
styles.add(ParagraphStyle(name='Small', parent=styles['BodyText'], fontSize=9, leading=12))
code_style = styles['Code']
code_style.fontSize = 8
code_style.leading = 10

story = []

def h1(t): story.append(Paragraph(t, styles['H1x']))
def h2(t): story.append(Paragraph(t, styles['H2x']))
def p(t): story.append(Paragraph(t, styles['Bodyx']))
def code(t): story.append(Preformatted(t, code_style)); story.append(Spacer(1, 6))

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 8)
    canvas.drawString(1.5*cm, 1*cm, 'LIU-2026 - Linux Administration and Docker Orchestration')
    canvas.drawRightString(19.5*cm, 1*cm, f'Page {doc.page}')
    canvas.restoreState()

# Page 1
story.append(Spacer(1, 2*cm))
story.append(Paragraph('Projet: Linux Administration and Docker Orchestration', styles['Title2']))
story.append(Paragraph('Objective: To master Linux administration and Docker orchestration', styles['H2x']))
story.append(Spacer(1, 1*cm))
p('Technical Challenge: Bash system management automation, CPU scheduling simulation using SRTF and Round Robin, and Docker deployment of a MySQL and Web multi-service stack.')
p('Prepared for: Dr. EL BENANY Mohamed Mahmoud - LIU-2026')
p('Slogan: Move from theory to action.')
story.append(Spacer(1, 2*cm))
rows = [['Deliverable', 'Content'], ['Git repository', 'Bash, Python, Docker files'], ['PDF report', 'Explanation, algorithms, steps, results'], ['Video demo', '3 minutes: run Bash, Python, Docker']]
t = Table(rows, colWidths=[5*cm, 10*cm])
t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#d9eaf7')),('GRID',(0,0),(-1,-1),0.5,colors.grey),('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),('VALIGN',(0,0),(-1,-1),'TOP')]))
story.append(t)
story.append(PageBreak())

# Page 2
h1('1. Introduction')
p('This project transforms operating system concepts into practical activities. It combines administration automation, CPU scheduling analysis, and service deployment using containers.')
p('The Bash part automates system management tasks. The CPU part simulates how an operating system chooses which process receives the processor. The Docker part deploys a web application connected to a MySQL database.')
h2('Project objectives')
p('The main objectives are: understand Linux commands, automate administration tasks, compare SRTF and Round Robin scheduling, deploy services with Docker Compose, and organize the work in a clean Git repository.')
h2('Tools used')
rows = [['Tool', 'Role'], ['Bash', 'Automate Linux system management'], ['Python', 'Simulate CPU scheduling algorithms'], ['Docker Compose', 'Deploy MySQL and Web services'], ['Git', 'Version control and collaboration']]
t=Table(rows, colWidths=[4*cm, 11*cm]); t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#d9eaf7')),('GRID',(0,0),(-1,-1),0.5,colors.grey),('FONTNAME',(0,0),(-1,0),'Helvetica-Bold')]))
story.append(t)
story.append(PageBreak())

# Page3 Bash
h1('2. Bash: System Management Automation')
p('Bash is a command language used in Linux. Instead of writing commands one by one, we create a script that executes them automatically. In this project, the script collects system information and saves it in a report file.')
h2('Tasks automated')
p('The script creates a reports directory, collects hostname, current user, uptime, operating system information, CPU usage, memory usage, disk usage, top processes, and network information.')
h2('Main Bash script')
code("""#!/bin/bash
REPORT_DIR="reports"
REPORT_FILE="$REPORT_DIR/system_report_$(date +%Y%m%d_%H%M%S).txt"
mkdir -p "$REPORT_DIR"
{
  echo "SYSTEM MANAGEMENT REPORT"
  echo "Date: $(date)"
  echo "Hostname: $(hostname)"
  echo "Current user: $(whoami)"
  echo "Uptime: $(uptime -p 2>/dev/null || uptime)"
  free -h
  df -h
  ps aux --sort=-%cpu | head -10
} > "$REPORT_FILE"
echo "Report generated successfully: $REPORT_FILE"""
)
h2('How to run it')
code('cd bash\nchmod +x system_management.sh\n./system_management.sh')
story.append(PageBreak())

# Page4 Bash explanation
h1('3. Bash Script Explanation')
p('The command mkdir -p creates the report folder only if it does not already exist. The variable REPORT_FILE contains the output file name with the current date and time. This avoids replacing old reports.')
p('The block between braces { ... } groups all outputs and redirects them into one file using >. Commands such as free -h, df -h, ps aux, top, ip addr and cat /etc/os-release are used to describe the current state of the system.')
h2('Expected result')
p('After execution, the user obtains a text file in the reports folder. This file can be included as evidence in the Git repository or shown during the video demo.')
h2('Why this is useful')
p('A system administrator often needs to monitor resources and collect diagnostic information. Automation saves time, reduces errors, and makes the task repeatable.')
story.append(PageBreak())

# Page5 CPU theory
h1('4. CPU Scheduling: Concept')
p('CPU scheduling is the mechanism used by the operating system to choose which process runs on the processor. Each process has an arrival time and a burst time. Arrival time means when the process becomes ready. Burst time means how long it needs the CPU.')
h2('Metrics')
rows=[['Metric','Meaning'],['Completion time','Time when the process finishes'],['Turnaround time','Completion time - Arrival time'],['Waiting time','Turnaround time - Burst time'],['Average waiting time','Mean waiting time for all processes']]
t=Table(rows, colWidths=[5*cm,10*cm]); t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#d9eaf7')),('GRID',(0,0),(-1,-1),0.5,colors.grey),('FONTNAME',(0,0),(-1,0),'Helvetica-Bold')]))
story.append(t)
h2('Dataset used in the simulation')
rows=[['Process','Arrival','Burst'],['P1','0','5'],['P2','1','3'],['P3','2','8'],['P4','3','6']]
t=Table(rows, colWidths=[5*cm,5*cm,5*cm]); t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#d9eaf7')),('GRID',(0,0),(-1,-1),0.5,colors.grey),('FONTNAME',(0,0),(-1,0),'Helvetica-Bold')]))
story.append(t)
story.append(PageBreak())

# Page6 SRTF
h1('5. SRTF Algorithm')
p('SRTF means Shortest Remaining Time First. It is a preemptive scheduling algorithm. At each unit of time, the CPU selects the available process with the smallest remaining time. If a new process arrives with a shorter remaining time, the current process can be interrupted.')
h2('Python idea')
p('The program keeps a remaining time for each process. At every time unit, it filters available processes and selects the one with the minimum remaining time.')
code("""available = [p for p in processes if p['arrival'] <= time and remaining[p['pid']] > 0]
current = min(available, key=lambda p: remaining[p['pid']])
remaining[current['pid']] -= 1
time += 1""")
h2('Advantages and limits')
p('SRTF gives good results for short processes because they finish quickly. However, long processes may wait too much if many short processes arrive.')
story.append(PageBreak())

# Page7 RR
h1('6. Round Robin Algorithm')
p('Round Robin gives each process the CPU for a fixed time called quantum. If the process is not finished after this time, it returns to the ready queue. This method is fair because every process gets a turn.')
h2('Python idea')
code("""ready = deque()
current = ready.popleft()
run_time = min(quantum, remaining[pid])
time += run_time
remaining[pid] -= run_time
if remaining[pid] > 0:
    ready.append(current)""")
h2('Quantum')
p('The quantum strongly affects the result. A very small quantum creates many context switches. A very large quantum makes Round Robin behave almost like FCFS.')
h2('Advantages and limits')
p('Round Robin is simple and fair. It is suitable for interactive systems, but average waiting time can be higher than SRTF.')
story.append(PageBreak())

# Page8 comparison
h1('7. SRTF vs Round Robin Comparison')
rows=[['Criterion','SRTF','Round Robin'],['Decision rule','Smallest remaining time','Fixed quantum and queue'],['Preemption','Yes','Yes'],['Fairness','Medium','High'],['Good for','Short processes','Interactive systems'],['Risk','Starvation of long jobs','Many context switches']]
t=Table(rows, colWidths=[4*cm,5.5*cm,5.5*cm]); t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#d9eaf7')),('GRID',(0,0),(-1,-1),0.5,colors.grey),('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),('VALIGN',(0,0),(-1,-1),'TOP')]))
story.append(t)
h2('What to show in the demo')
p('Run round_robin.py and srtf.py, show the Gantt chart, show waiting time and turnaround time, then explain which algorithm is more suitable depending on the goal: performance for short jobs or fairness between processes.')
story.append(PageBreak())

# Page9 Docker
h1('8. Docker Multi-Service Stack')
p('Docker Compose is used to deploy two services: a MySQL database and a Python Flask web application. The web service connects to the database using environment variables. This demonstrates orchestration of multiple services.')
h2('docker-compose.yml')
code("""services:
  db:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: root_password_fst
      MYSQL_DATABASE: liu_db
    ports:
      - "3306:3306"
  web:
    build: ./web
    depends_on:
      - db
    ports:
      - "5000:5000"""
)
h2('Run commands')
code('cd docker\ndocker compose up -d --build\ndocker compose ps\n# Browser: http://localhost:5000\ndocker compose down')
story.append(PageBreak())

# Page10 Org/demo conclusion
h1('9. Organization, Video Demo and Conclusion')
h2('Suggested group organization')
rows=[['Student','Task'],['Student 1','Bash automation and report screenshots'],['Student 2','Python CPU scheduling: SRTF and Round Robin'],['Student 3','Docker Compose stack and Git repository organization']]
t=Table(rows, colWidths=[4*cm,11*cm]); t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#d9eaf7')),('GRID',(0,0),(-1,-1),0.5,colors.grey),('FONTNAME',(0,0),(-1,0),'Helvetica-Bold')]))
story.append(t)
h2('3-minute video plan')
p('Minute 1: explain objective and run Bash script. Minute 2: run Python simulations and compare results. Minute 3: run Docker Compose and open the web application in the browser.')
h2('Conclusion')
p('This project connects theory with practice. Bash demonstrates automation, Python demonstrates CPU scheduling behavior, and Docker demonstrates deployment of real services. The final result is a clean, reproducible and demonstrable system administration project.')
h2('Repository structure')
code('project/\n  bash/system_management.sh\n  python/round_robin.py\n  python/srtf.py\n  docker/docker-compose.yml\n  docker/web/Dockerfile\n  docs/LIU2026_Report.pdf\n  README.md')

doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(pdf_path)
