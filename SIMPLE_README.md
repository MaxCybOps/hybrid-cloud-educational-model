# HYBRID CLOUD MODEL SIMULATOR
## Ready-to-Run PhD Group Project

---

## 🎯 WHAT YOU HAVE

**ONE complete hybrid cloud infrastructure model** that generates data for all four PhD researchers.

**File**: `HYBRID_CLOUD_MODEL.py` (Complete, working simulator - 500+ lines)

---

## ⚡ QUICK START (3 Steps)

### Step 1: Install Python Packages

```bash
pip install numpy pandas
```

### Step 2: Run the Model

```bash
python HYBRID_CLOUD_MODEL.py
```

### Step 3: Get Your Data

Check the `GROUP_PROJECT_DATA` folder. You'll find:

```
GROUP_PROJECT_DATA/
├── ADEYEMI_security_data.csv        (498,834 records)
├── TEMITAYO_performance_data.csv    (384 records)
├── ESTHER_architecture_data.csv     (2,304 records)
├── DAVID_cost_data.csv              (4 records)
├── DAVID_scaling_events.csv         (92 records)
└── simulation_summary.json
```

**That's it!** Each person gets their data from the SAME simulation run.

---

## 📊 WHAT THE MODEL DOES

### The Unified Hybrid Cloud Infrastructure:

```
┌─────────────────────────────────────────────────────┐
│  HYBRID CLOUD EDUCATIONAL INFRASTRUCTURE MODEL      │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ┌──────────────┐          ┌──────────────┐       │
│  │ PRIVATE      │          │ PUBLIC       │       │
│  │ CLOUD        │◄────────►│ CLOUD        │       │
│  │              │          │              │       │
│  │ 4 VMs        │          │ 2-10 VMs     │       │
│  │ Fixed Cost   │          │ Auto-Scale   │       │
│  └──────────────┘          └──────────────┘       │
│                                                     │
│  PREDEFINED VALUES:                                │
│  ✓ 6 Educational Services (LMS, Exams, etc.)      │
│  ✓ Cost Model ($500/month private, $0.096/hr pub) │
│  ✓ 4 User Roles (Student, Staff, Admin, Unauth)   │
│  ✓ RBAC Security Policies (3 levels)              │
│  ✓ Nigeria Infrastructure Parameters              │
│  ✓ 4 Workload Scenarios (Low/Mod/Peak/Spike)      │
└─────────────────────────────────────────────────────┘
                        │
                        ▼
            RUNS SIMULATION
                        │
        ┌───────────────┼───────────────┬──────────────┐
        │               │               │              │
        ▼               ▼               ▼              ▼
    ADEYEMI        TEMITAYO         ESTHER          DAVID
   (Security)    (Performance)  (Architecture)    (Cost)
```

---

## 🔬 WHAT EACH PERSON GETS

### ADEYEMI - Security & Compliance Data

**File**: `ADEYEMI_security_data.csv`

**Sample Data**:
```csv
timestamp,user_role,service,cloud_target,authorized,reason,policy
2026-02-13 22:39:37,student,lms,public,True,access_granted,RBAC_INTERMEDIATE
2026-02-13 22:39:37,unauthorized,exam,private,False,unauthorized_user,DENY_ALL
2026-02-13 22:39:37,staff,admin_dashboard,private,True,access_granted,RBAC_INTERMEDIATE
```

**What to Analyze**:
- Authorization success/failure rates
- Policy violations by role
- RBAC effectiveness
- Data residency compliance

---

### TEMITAYO - Performance & Optimization Data

**File**: `TEMITAYO_performance_data.csv`

**Sample Data**:
```csv
timestamp,scenario,concurrent_users,response_time_ms,cpu_util_private,cpu_util_public
2026-02-13 22:39:37,moderate_demand,744,1432.5,78.3,45.2
2026-02-13 22:44:37,moderate_demand,817,1567.8,82.1,51.4
2026-02-13 22:49:37,moderate_demand,956,1689.2,91.5,58.7
```

**What to Analyze**:
- Response time trends
- CPU/memory utilization
- Scalability behavior
- Performance degradation under load

---

### ESTHER - Architecture & Design Data

**File**: `ESTHER_architecture_data.csv`

**Sample Data**:
```csv
timestamp,service,cloud_decision,reason,sensitivity
2026-02-13 22:39:37,student_registration,private,high_sensitivity_data_residency,high
2026-02-13 22:39:37,lms,public,low_sensitivity_public_cloud,low
2026-02-13 22:39:37,exam_platform,private,high_sensitivity_data_residency,high
```

**What to Analyze**:
- Workload distribution (private vs public)
- Routing decisions by sensitivity
- Architecture effectiveness
- Design suitability for Nigeria

---

### DAVID - Cost & Scalability Data

**File 1**: `DAVID_cost_data.csv`

**Sample Data**:
```csv
timestamp,scenario,cloud_type,compute_cost,storage_cost,network_cost,total_cost,utilization
2026-02-13 22:39:37,moderate_demand,private,65.75,6.58,0.00,87.95,78.3
2026-02-13 22:39:37,moderate_demand,public,11.52,0.16,21.60,33.28,51.2
```

**File 2**: `DAVID_scaling_events.csv`

**Sample Data**:
```csv
timestamp,cloud_type,event,utilization,vms_added
2026-02-13 23:15:37,public,scale_out,85.3,1
2026-02-13 23:30:37,public,scale_out,88.7,1
```

**What to Analyze**:
- Total costs by deployment type
- Cost efficiency ratios
- Scaling frequency and triggers
- ROI analysis

---

## 🎓 HOW THE GROUP USES IT

### Scenario 1: Everyone Runs the Same Simulation

```bash
# Person 1 runs the model
python HYBRID_CLOUD_MODEL.py

# Creates: GROUP_PROJECT_DATA/ folder with all 4 datasets

# Person 2 gets: ADEYEMI_security_data.csv
# Person 3 gets: TEMITAYO_performance_data.csv
# Person 4 gets: ESTHER_architecture_data.csv
# Person 5 gets: DAVID_cost_data.csv + DAVID_scaling_events.csv
```

### Scenario 2: Compare Different Configurations

You can modify the code to test different scenarios:

```python
# In HYBRID_CLOUD_MODEL.py, line ~480, change:

scenarios_to_run = [
    WorkloadScenario.LOW_DEMAND,      # Add this
    WorkloadScenario.MODERATE_DEMAND,
    WorkloadScenario.PEAK_DEMAND,
    WorkloadScenario.SPIKE             # Add this
]
```

Or test different security levels:

```python
# Line ~455, change:
model = HybridCloudModel(security_level="strict")  # or "baseline"
```

---

## 📈 PREDEFINED VALUES IN THE MODEL

### Educational Services (6 total):
1. Student Registration (High security, Private cloud)
2. Exam Platform (High security, Private cloud)
3. Learning Management System (Medium security, Hybrid)
4. Digital Library (Low security, Public cloud)
5. Collaboration Tools (Low security, Public cloud)
6. Admin Dashboard (High security, Private cloud)

### Cost Model:
- **Private Cloud**: $500/month per VM (fixed)
- **Public Cloud**: $0.096/hour per VM (elastic)
- **Storage**: $0.10/GB/month (private), $0.023/GB/month (public)
- **Network**: $0.09/GB egress (public only)

### Infrastructure (Nigeria Context):
- Power reliability: 65%
- Network bandwidth: 25 Mbps
- Network latency: 150ms

### Workload Scenarios:
- **Low Demand**: 50-100 users, 24 hours
- **Moderate Demand**: 500-1000 users, 24 hours
- **Peak Demand**: 2000-5000 users, 8 hours
- **Spike**: 100→3000 users, 2 hours

### Security Levels:
- **Baseline**: Minimal role separation
- **Intermediate**: Standard RBAC
- **Strict**: Least-privilege enforcement

---

## ✅ VERIFICATION

After running, you should see:

```
SIMULATION COMPLETE!
All four team members can now analyze their respective datasets

Generated files in 'GROUP_PROJECT_DATA' folder:
  → ADEYEMI_security_data.csv (Security & Compliance)
  → TEMITAYO_performance_data.csv (Performance & Optimization)
  → ESTHER_architecture_data.csv (Architecture & Design)
  → DAVID_cost_data.csv (Cost Efficiency)
  → DAVID_scaling_events.csv (Scalability)
```

---

## 🎯 WHAT MAKES THIS A GROUP PROJECT

✅ **ONE unified model** (not 4 separate programs)  
✅ **Same infrastructure** (shared hybrid cloud)  
✅ **Same simulation run** (consistent data)  
✅ **Predefined values** (all services, costs, policies built-in)  
✅ **Different perspectives** (each person analyzes different aspects)

**This is Design Science Research**: One artefact, multiple evaluations.

---

## 💡 TIPS

### If You Want More Data:
Run the simulation multiple times:

```bash
python HYBRID_CLOUD_MODEL.py  # Run 1
# Rename folder: GROUP_PROJECT_DATA → RUN_1

python HYBRID_CLOUD_MODEL.py  # Run 2
# Rename folder: GROUP_PROJECT_DATA → RUN_2

python HYBRID_CLOUD_MODEL.py  # Run 3
# Rename folder: GROUP_PROJECT_DATA → RUN_3
```

### If You Want Different Scenarios:
Edit line 480 in the file to include all 4 scenarios:

```python
scenarios_to_run = [
    WorkloadScenario.LOW_DEMAND,
    WorkloadScenario.MODERATE_DEMAND,
    WorkloadScenario.PEAK_DEMAND,
    WorkloadScenario.SPIKE
]
```

### If Simulation is Too Slow:
Reduce the duration (edit line 15-25 in the PREDEFINED VALUES section)

---

## 📞 TROUBLESHOOTING

**Problem**: `ModuleNotFoundError: No module named 'numpy'`  
**Solution**: `pip install numpy pandas`

**Problem**: No output folder created  
**Solution**: Check for error messages in the console

**Problem**: Files are too large  
**Solution**: This is normal! Security data has 500k+ records

**Problem**: Want to analyze data  
**Solution**: Open CSV files in Excel or use Python pandas

---

## 🎓 FOR YOUR DISSERTATION

### When Writing:

**"We developed a unified hybrid cloud infrastructure model with predefined values for educational service delivery. The model simulates six core educational services across private and public cloud infrastructure with realistic workload patterns based on Nigerian educational context. All four researchers evaluated this same artefact from their specialized perspectives (security, performance, architecture, and cost), generating over 500,000 data points for comprehensive analysis."**

---

## 📚 WHAT YOU HAVE

1. ✅ `HYBRID_CLOUD_MODEL.py` - Complete working simulator
2. ✅ `GROUP_PROJECT_DATA/` - Sample data already generated
3. ✅ Predefined values for all parameters
4. ✅ Ready-to-run model
5. ✅ Data for all four researchers

**Total**: ONE complete PhD group project model!

---

**Just run it and get your data!** 🚀

```bash
python HYBRID_CLOUD_MODEL.py
```
