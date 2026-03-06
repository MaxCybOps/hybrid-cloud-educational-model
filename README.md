# Hybrid Cloud Educational Infrastructure Simulator

> A comprehensive Python-based simulation model for evaluating hybrid cloud deployment in educational institutions.

## 📚 PhD Research Project

**Title**: "Enhancing Educational Service Delivery through Cloud-Based Digital Infrastructure"

**Authors**: PhD Research Group, University of the West of Scotland

## 🎯 Overview

This is a unified hybrid cloud infrastructure model that generates data for four specialized research perspectives:

1. **Security & Compliance** - RBAC and data residency analysis
2. **Performance & Optimization** - Response time and scalability metrics
3. **Architecture & Design** - Workload routing and infrastructure evaluation
4. **Cost Efficiency** - Resource utilization and financial analysis

## 🚀 Quick Start

### Installation
```bash
pip install numpy pandas
```

### Run Simulation
```bash
python HYBRID_CLOUD_MODEL.py
```

### Output

The model generates five datasets in `GROUP_PROJECT_DATA/` folder:
- `ADEYEMI_security_data.csv` (498,834 records)
- `TEMITAYO_performance_data.csv` (384 records)
- `ESTHER_architecture_data.csv` (2,304 records)
- `DAVID_cost_data.csv` (4 records)
- `DAVID_scaling_events.csv` (92 records)

## 🏗️ Model Architecture

The simulator implements a complete hybrid cloud infrastructure with:

- **6 Educational Services**: Registration, Exams, LMS, Library, Collaboration, Admin
- **Hybrid Deployment**: 4 Private VMs + Auto-scaling Public VMs
- **Cost Model**: $500/month private, $0.096/hour public
- **Security**: RBAC with 4 user roles (Student, Staff, Admin, Unauthorized)
- **Infrastructure Context**: Nigeria parameters (25 Mbps, 65% power reliability)
- **Workload Scenarios**: Low, Moderate, Peak, and Spike demand

## 📊 Predefined Values

All infrastructure parameters are predefined in the model:

- Educational services with sensitivity classifications
- Cost models for private and public cloud
- RBAC security policies (Baseline, Intermediate, Strict)
- Nigerian infrastructure constraints
- Realistic workload patterns

## 📖 Documentation

- **SIMPLE_README.md** - Quick usage guide
- **VISUAL_GUIDE.md** - Architecture diagrams and flow charts

## 🎓 Academic Use

This model supports Design Science Research methodology for evaluating hybrid cloud infrastructure in educational contexts.

### Citation
```bibtex
@software{hybrid_cloud_model_2026,
  title={Hybrid Cloud Educational Infrastructure Simulator},
  author={[Your Research Group]},
  year={2026},
  institution={University of the West of Scotland},
  url={https://github.com/YOUR-USERNAME/hybrid-cloud-educational-model}
}
```

## 📄 License

MIT License - See LICENSE file for details

## 🤝 Contributing

This is an academic research project. For questions or collaboration:
- Open an issue
- Contact: [your.email@university.ac.uk]

## 🔬 Research Outputs

This simulator generates empirical data for PhD research on:
- Hybrid cloud cost efficiency vs pure deployments
- RBAC effectiveness in educational cloud systems
- Architectural suitability for developing regions
- Performance optimization strategies

---

**Made with ❤️ for advancing educational technology research**
