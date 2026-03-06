"""
================================================================================
HYBRID CLOUD EDUCATIONAL INFRASTRUCTURE SIMULATOR
================================================================================
Complete Model for Group Project
Title: "Enhancing Educational Service Delivery through Cloud-Based Digital Infrastructure"

This is THE unified artefact that all four researchers use together.
- ONE model with predefined values
- Generates data for ALL four specializations
- Ready to run immediately

Author: Group Research 
Date: February 2026
================================================================================
"""

import numpy as np
import pandas as pd
import random
import json
from datetime import datetime, timedelta
from enum import Enum
from dataclasses import dataclass
from typing import List, Dict, Tuple
import os
import warnings
warnings.filterwarnings('ignore')

print("="*80)
print(" HYBRID CLOUD EDUCATIONAL INFRASTRUCTURE SIMULATOR")
print(" Loading model components...")
print("="*80)

# ============================================================================
# ENUMERATIONS
# ============================================================================

class CloudType(Enum):
    PRIVATE = "private"
    PUBLIC = "public"
    HYBRID = "hybrid"

class ServiceType(Enum):
    STUDENT_REGISTRATION = "student_registration"
    EXAM_PLATFORM = "exam_platform"
    LMS = "learning_management_system"
    DIGITAL_LIBRARY = "digital_library"
    COLLABORATION = "collaboration_tools"
    ADMIN_DASHBOARD = "admin_dashboard"

class UserRole(Enum):
    STUDENT = "student"
    STAFF = "staff"
    ADMINISTRATOR = "administrator"
    UNAUTHORIZED = "unauthorized"

class SecurityLevel(Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

class WorkloadScenario(Enum):
    LOW_DEMAND = "low_demand"
    MODERATE_DEMAND = "moderate_demand"
    PEAK_DEMAND = "peak_demand"
    SPIKE = "spike"

# ============================================================================
# PREDEFINED VALUES - THE HYBRID CLOUD MODEL
# ============================================================================

class PredefinedValues:
    """All predefined values for the hybrid cloud model"""
    
    # Educational Services Configuration
    SERVICES = {
        ServiceType.STUDENT_REGISTRATION: {
            'sensitivity': SecurityLevel.HIGH,
            'preferred_cloud': CloudType.PRIVATE,
            'cpu_cores': 4,
            'memory_mb': 8192,
            'storage_gb': 500,
            'base_response_time_ms': 200,
            'allowed_roles': [UserRole.STUDENT, UserRole.STAFF, UserRole.ADMINISTRATOR]
        },
        ServiceType.EXAM_PLATFORM: {
            'sensitivity': SecurityLevel.HIGH,
            'preferred_cloud': CloudType.PRIVATE,
            'cpu_cores': 8,
            'memory_mb': 16384,
            'storage_gb': 1000,
            'base_response_time_ms': 150,
            'allowed_roles': [UserRole.STUDENT, UserRole.STAFF, UserRole.ADMINISTRATOR]
        },
        ServiceType.LMS: {
            'sensitivity': SecurityLevel.MEDIUM,
            'preferred_cloud': CloudType.HYBRID,
            'cpu_cores': 4,
            'memory_mb': 8192,
            'storage_gb': 2000,
            'base_response_time_ms': 300,
            'allowed_roles': [UserRole.STUDENT, UserRole.STAFF, UserRole.ADMINISTRATOR]
        },
        ServiceType.DIGITAL_LIBRARY: {
            'sensitivity': SecurityLevel.LOW,
            'preferred_cloud': CloudType.PUBLIC,
            'cpu_cores': 2,
            'memory_mb': 4096,
            'storage_gb': 5000,
            'base_response_time_ms': 400,
            'allowed_roles': [UserRole.STUDENT, UserRole.STAFF, UserRole.ADMINISTRATOR]
        },
        ServiceType.COLLABORATION: {
            'sensitivity': SecurityLevel.LOW,
            'preferred_cloud': CloudType.PUBLIC,
            'cpu_cores': 2,
            'memory_mb': 4096,
            'storage_gb': 1000,
            'base_response_time_ms': 250,
            'allowed_roles': [UserRole.STUDENT, UserRole.STAFF, UserRole.ADMINISTRATOR]
        },
        ServiceType.ADMIN_DASHBOARD: {
            'sensitivity': SecurityLevel.HIGH,
            'preferred_cloud': CloudType.PRIVATE,
            'cpu_cores': 2,
            'memory_mb': 4096,
            'storage_gb': 200,
            'base_response_time_ms': 180,
            'allowed_roles': [UserRole.STAFF, UserRole.ADMINISTRATOR]
        }
    }
    
    # Cost Model (Predefined)
    COST_PRIVATE_VM_MONTHLY = 500  # USD
    COST_PRIVATE_STORAGE_GB_MONTHLY = 0.10
    COST_PRIVATE_POWER_KWH = 0.12
    COST_PUBLIC_VM_HOURLY = 0.096
    COST_PUBLIC_STORAGE_GB_MONTHLY = 0.023
    COST_PUBLIC_NETWORK_GB = 0.09
    
    # Infrastructure Context (Nigeria)
    NIGERIA_POWER_RELIABILITY = 0.65
    NIGERIA_BANDWIDTH_MBPS = 25
    NIGERIA_LATENCY_MS = 150
    
    # Workload Scenarios (Predefined)
    SCENARIOS = {
        WorkloadScenario.LOW_DEMAND: {
            'min_users': 50, 'max_users': 100, 'duration_hours': 24
        },
        WorkloadScenario.MODERATE_DEMAND: {
            'min_users': 500, 'max_users': 1000, 'duration_hours': 24
        },
        WorkloadScenario.PEAK_DEMAND: {
            'min_users': 2000, 'max_users': 5000, 'duration_hours': 8
        },
        WorkloadScenario.SPIKE: {
            'min_users': 100, 'max_users': 3000, 'duration_hours': 2
        }
    }
    
    # Security Policies (RBAC - Predefined)
    RBAC_POLICIES = {
        'baseline': {
            UserRole.STUDENT: ['lms', 'library', 'collaboration'],
            UserRole.STAFF: 'all',
            UserRole.ADMINISTRATOR: 'all'
        },
        'intermediate': {
            UserRole.STUDENT: ['registration', 'lms', 'library', 'collaboration'],
            UserRole.STAFF: ['registration', 'exam', 'lms', 'library', 'collaboration', 'admin'],
            UserRole.ADMINISTRATOR: 'all'
        },
        'strict': {
            UserRole.STUDENT: ['lms', 'library', 'collaboration'],
            UserRole.STAFF: ['exam', 'lms', 'library', 'collaboration'],
            UserRole.ADMINISTRATOR: 'all'
        }
    }

print("✓ Predefined values loaded")
print("  - 6 Educational Services configured")
print("  - Cost models loaded (Private: $500/month, Public: $0.096/hour)")
print("  - Nigeria infrastructure parameters set")
print("  - 4 Workload scenarios defined")
print("  - 3 RBAC security levels configured")

# ============================================================================
# HYBRID CLOUD INFRASTRUCTURE MODEL
# ============================================================================

class HybridCloudModel:
    """
    THE unified hybrid cloud infrastructure model
    This is the single artefact that all four PhD students evaluate
    """
    
    def __init__(self, security_level="intermediate"):
        self.deployment = CloudType.HYBRID
        self.security_level = security_level
        
        # Infrastructure state
        self.private_vms = []
        self.public_vms = []
        self.vm_counter = 0
        
        # Data collection for all four specializations
        self.security_logs = []      # For Adeyemi
        self.performance_data = []   # For Temitayo
        self.cost_data = []          # For David
        self.architecture_data = []  # For Esther
        self.scaling_events = []     # For David
        
        # Simulation time
        self.current_time = datetime.now()
        self.simulation_start = datetime.now()
        
        # Initialize the infrastructure
        self._initialize_infrastructure()
        
    def _initialize_infrastructure(self):
        """Set up base infrastructure with predefined capacity"""
        print("\nInitializing Hybrid Cloud Infrastructure...")
        
        # Private Cloud: 4 base VMs (predefined)
        for i in range(4):
            self.private_vms.append({
                'id': f'PRIVATE_VM_{i+1:02d}',
                'cpu_cores': 4,
                'memory_mb': 8192,
                'storage_gb': 500,
                'cost_per_hour': PredefinedValues.COST_PRIVATE_VM_MONTHLY / 730,
                'utilization': 0.0,
                'active': True
            })
        
        # Public Cloud: 2 base VMs (predefined)
        for i in range(2):
            self.public_vms.append({
                'id': f'PUBLIC_VM_{i+1:02d}',
                'cpu_cores': 4,
                'memory_mb': 8192,
                'storage_gb': 0,
                'cost_per_hour': PredefinedValues.COST_PUBLIC_VM_HOURLY,
                'utilization': 0.0,
                'active': True
            })
        
        print(f"  ✓ Private Cloud: {len(self.private_vms)} VMs provisioned")
        print(f"  ✓ Public Cloud: {len(self.public_vms)} VMs provisioned")
        print(f"  ✓ Security Level: {self.security_level}")
    
    def route_workload(self, service_type, timestamp):
        """
        Hybrid cloud routing logic (predefined algorithm)
        Routes workloads based on data sensitivity
        """
        service_config = PredefinedValues.SERVICES[service_type]
        sensitivity = service_config['sensitivity']
        
        # ROUTING DECISION LOGIC (Predefined)
        if sensitivity == SecurityLevel.HIGH:
            decision = CloudType.PRIVATE
            reason = "high_sensitivity_data_residency"
        elif sensitivity == SecurityLevel.MEDIUM:
            # Check private cloud capacity
            private_util = np.mean([vm['utilization'] for vm in self.private_vms if vm['active']])
            if private_util < 70:
                decision = CloudType.PRIVATE
                reason = "medium_sensitivity_private_available"
            else:
                decision = CloudType.PUBLIC
                reason = "medium_sensitivity_overflow"
        else:  # LOW
            decision = CloudType.PUBLIC
            reason = "low_sensitivity_public_cloud"
        
        # LOG FOR ESTHER (Architecture Data)
        self.architecture_data.append({
            'timestamp': timestamp,
            'service': service_type.value,
            'cloud_decision': decision.value,
            'reason': reason,
            'sensitivity': sensitivity.value
        })
        
        return decision
    
    def check_access(self, role, service_type, cloud_type, timestamp):
        """
        Security access control (predefined RBAC)
        Returns: (authorized, reason)
        """
        if role == UserRole.UNAUTHORIZED:
            # LOG FOR ADEYEMI (Security Data)
            self.security_logs.append({
                'timestamp': timestamp,
                'user_role': role.value,
                'service': service_type.value,
                'cloud_target': cloud_type.value,
                'authorized': False,
                'reason': 'unauthorized_user',
                'policy': 'DENY_ALL'
            })
            return False, "unauthorized"
        
        # Get RBAC policy
        policies = PredefinedValues.RBAC_POLICIES[self.security_level]
        user_policy = policies.get(role, [])
        
        # Check if service allowed
        service_name = service_type.value.split('_')[0]
        authorized = (user_policy == 'all' or service_name in str(user_policy))
        
        # Check cloud access restrictions
        if self.security_level == 'strict' and cloud_type == CloudType.PRIVATE:
            if role == UserRole.STUDENT:
                authorized = False
        
        # LOG FOR ADEYEMI (Security Data)
        self.security_logs.append({
            'timestamp': timestamp,
            'user_role': role.value,
            'service': service_type.value,
            'cloud_target': cloud_type.value,
            'authorized': authorized,
            'reason': 'access_granted' if authorized else 'policy_violation',
            'policy': f'RBAC_{self.security_level.upper()}'
        })
        
        return authorized, "granted" if authorized else "denied"
    
    def calculate_performance(self, users, service_type, cloud_type, timestamp):
        """
        Calculate performance metrics (predefined formulas)
        """
        service_config = PredefinedValues.SERVICES[service_type]
        base_time = service_config['base_response_time_ms']
        
        # Load factor
        vms = self.private_vms if cloud_type == CloudType.PRIVATE else self.public_vms
        active_vms = [vm for vm in vms if vm['active']]
        vm_count = len(active_vms) if active_vms else 1
        
        load_factor = users / (vm_count * 100)
        load_penalty = base_time * min(load_factor, 3.0)
        
        # Infrastructure penalty (Nigeria context)
        latency = PredefinedValues.NIGERIA_LATENCY_MS
        reliability_factor = 2.0 - PredefinedValues.NIGERIA_POWER_RELIABILITY
        
        # Calculate final response time
        response_time = (base_time + latency + load_penalty) * reliability_factor
        response_time = response_time * random.uniform(0.9, 1.1)  # Variance
        
        # Calculate utilization
        base_util = (users / (vm_count * 100)) * 100
        private_util = min(100, base_util * 1.2) if cloud_type == CloudType.PRIVATE else 0
        public_util = min(100, base_util * 0.8) if cloud_type == CloudType.PUBLIC else 0
        
        # Update VM utilization
        for vm in active_vms:
            vm['utilization'] = base_util + random.uniform(-10, 10)
            vm['utilization'] = max(0, min(100, vm['utilization']))
        
        return response_time, private_util, public_util
    
    def calculate_costs(self, duration_hours, scenario):
        """
        Calculate infrastructure costs (predefined cost model)
        """
        # Private cloud costs
        private_active = len([vm for vm in self.private_vms if vm['active']])
        private_util = np.mean([vm['utilization'] for vm in self.private_vms if vm['active']])
        
        private_compute = private_active * (PredefinedValues.COST_PRIVATE_VM_MONTHLY / 730) * duration_hours
        private_storage = 500 * (PredefinedValues.COST_PRIVATE_STORAGE_GB_MONTHLY / 730) * duration_hours
        private_power = private_active * 0.5 * PredefinedValues.COST_PRIVATE_POWER_KWH * duration_hours
        private_total = private_compute + private_storage + private_power
        
        # LOG FOR DAVID (Cost Data)
        self.cost_data.append({
            'timestamp': self.current_time,
            'scenario': scenario.value,
            'cloud_type': 'private',
            'compute_cost': private_compute,
            'storage_cost': private_storage,
            'network_cost': 0.0,
            'total_cost': private_total,
            'utilization': private_util
        })
        
        # Public cloud costs
        public_active = len([vm for vm in self.public_vms if vm['active']])
        public_util = np.mean([vm['utilization'] for vm in self.public_vms if vm['active']])
        
        public_compute = public_active * PredefinedValues.COST_PUBLIC_VM_HOURLY * duration_hours
        public_storage = 100 * (PredefinedValues.COST_PUBLIC_STORAGE_GB_MONTHLY / 730) * duration_hours
        public_network = duration_hours * 10 * PredefinedValues.COST_PUBLIC_NETWORK_GB
        public_total = public_compute + public_storage + public_network
        
        # LOG FOR DAVID (Cost Data)
        self.cost_data.append({
            'timestamp': self.current_time,
            'scenario': scenario.value,
            'cloud_type': 'public',
            'compute_cost': public_compute,
            'storage_cost': public_storage,
            'network_cost': public_network,
            'total_cost': public_total,
            'utilization': public_util
        })
        
        return private_total + public_total
    
    def auto_scale(self, cloud_type, utilization, timestamp):
        """Auto-scaling based on utilization (predefined thresholds)"""
        if cloud_type == CloudType.PRIVATE:
            # Private cloud has fixed capacity
            if utilization > 90:
                self.scaling_events.append({
                    'timestamp': timestamp,
                    'cloud_type': 'private',
                    'event': 'capacity_limit_reached',
                    'utilization': utilization
                })
            return
        
        # Public cloud can scale
        if utilization > 80:
            # Scale out
            new_vm = {
                'id': f'PUBLIC_VM_SCALED_{len(self.public_vms)+1:02d}',
                'cpu_cores': 4,
                'memory_mb': 8192,
                'storage_gb': 0,
                'cost_per_hour': PredefinedValues.COST_PUBLIC_VM_HOURLY,
                'utilization': 0.0,
                'active': True
            }
            self.public_vms.append(new_vm)
            
            self.scaling_events.append({
                'timestamp': timestamp,
                'cloud_type': 'public',
                'event': 'scale_out',
                'utilization': utilization,
                'vms_added': 1
            })
    
    def simulate_scenario(self, scenario, verbose=True):
        """
        Run a complete scenario simulation
        This generates data for ALL four specializations
        """
        config = PredefinedValues.SCENARIOS[scenario]
        duration_hours = config['duration_hours']
        duration_minutes = duration_hours * 60
        
        if verbose:
            print(f"\n{'='*70}")
            print(f"SIMULATING: {scenario.value}")
            print(f"Duration: {duration_hours} hours")
            print(f"Expected users: {config['min_users']}-{config['max_users']}")
            print(f"{'='*70}\n")
        
        # Generate workload pattern
        measurement_points = duration_minutes // 5  # Every 5 minutes
        
        for point in range(measurement_points):
            minute = point * 5
            self.current_time = self.simulation_start + timedelta(minutes=minute)
            
            # Generate user load
            avg_users = random.randint(config['min_users'], config['max_users'])
            
            # Simulate service requests
            services_used = list(ServiceType)
            
            total_requests = 0
            total_response_time = 0
            
            for service_type in services_used:
                requests = int(avg_users * 0.15)  # 15% of users per service
                
                # Route workload
                cloud = self.route_workload(service_type, self.current_time)
                
                # Simulate user access attempts
                for _ in range(requests):
                    # Random user role
                    role_choice = random.choices(
                        [UserRole.STUDENT, UserRole.STAFF, UserRole.ADMINISTRATOR, UserRole.UNAUTHORIZED],
                        weights=[70, 20, 8, 2]
                    )[0]
                    
                    # Check access (SECURITY DATA)
                    self.check_access(role_choice, service_type, cloud, self.current_time)
                
                # Calculate performance (PERFORMANCE DATA)
                response_time, priv_util, pub_util = self.calculate_performance(
                    requests, service_type, cloud, self.current_time
                )
                
                total_requests += requests
                total_response_time += response_time * requests
            
            # Record performance metrics
            avg_response = total_response_time / total_requests if total_requests > 0 else 0
            
            private_util = np.mean([vm['utilization'] for vm in self.private_vms if vm['active']])
            public_util = np.mean([vm['utilization'] for vm in self.public_vms if vm['active']])
            
            # LOG FOR TEMITAYO (Performance Data)
            self.performance_data.append({
                'timestamp': self.current_time,
                'scenario': scenario.value,
                'concurrent_users': avg_users,
                'response_time_ms': avg_response,
                'cpu_util_private': private_util,
                'cpu_util_public': public_util,
                'active_vms_private': len([vm for vm in self.private_vms if vm['active']]),
                'active_vms_public': len([vm for vm in self.public_vms if vm['active']])
            })
            
            # Auto-scale based on utilization
            self.auto_scale(CloudType.PRIVATE, private_util, self.current_time)
            self.auto_scale(CloudType.PUBLIC, public_util, self.current_time)
            
            # Progress
            if verbose and minute % 60 == 0:
                progress = (minute / duration_minutes) * 100
                print(f"Progress: {progress:.0f}% | Users: {avg_users} | Requests: {total_requests}")
        
        # Calculate costs for entire scenario
        self.calculate_costs(duration_hours, scenario)
        
        if verbose:
            print(f"\n{'='*70}")
            print(f"SCENARIO COMPLETE: {scenario.value}")
            print(f"  Security events: {len(self.security_logs):,}")
            print(f"  Performance measurements: {len(self.performance_data):,}")
            print(f"  Architecture decisions: {len(self.architecture_data):,}")
            print(f"  Cost records: {len(self.cost_data):,}")
            print(f"  Scaling events: {len(self.scaling_events):,}")
            print(f"{'='*70}\n")
    
    def export_data(self, output_dir="simulation_results"):
        """Export all data for the four specializations"""
        os.makedirs(output_dir, exist_ok=True)
        
        print(f"\nExporting data to: {output_dir}/\n")
        
        # ADEYEMI - Security Data
        if self.security_logs:
            df = pd.DataFrame(self.security_logs)
            filename = f"{output_dir}/ADEYEMI_security_data.csv"
            df.to_csv(filename, index=False)
            print(f"✓ ADEYEMI (Security): {len(df):,} records → {filename}")
        
        # TEMITAYO - Performance Data
        if self.performance_data:
            df = pd.DataFrame(self.performance_data)
            filename = f"{output_dir}/TEMITAYO_performance_data.csv"
            df.to_csv(filename, index=False)
            print(f"✓ TEMITAYO (Performance): {len(df):,} records → {filename}")
        
        # ESTHER - Architecture Data
        if self.architecture_data:
            df = pd.DataFrame(self.architecture_data)
            filename = f"{output_dir}/ESTHER_architecture_data.csv"
            df.to_csv(filename, index=False)
            print(f"✓ ESTHER (Architecture): {len(df):,} records → {filename}")
        
        # DAVID - Cost & Scaling Data
        if self.cost_data:
            df = pd.DataFrame(self.cost_data)
            filename = f"{output_dir}/DAVID_cost_data.csv"
            df.to_csv(filename, index=False)
            print(f"✓ DAVID (Cost): {len(df):,} records → {filename}")
        
        if self.scaling_events:
            df = pd.DataFrame(self.scaling_events)
            filename = f"{output_dir}/DAVID_scaling_events.csv"
            df.to_csv(filename, index=False)
            print(f"✓ DAVID (Scaling): {len(df):,} records → {filename}")
        
        # Summary
        summary = {
            'model': 'Hybrid Cloud Educational Infrastructure',
            'deployment': self.deployment.value,
            'security_level': self.security_level,
            'simulation_start': self.simulation_start.isoformat(),
            'simulation_end': self.current_time.isoformat(),
            'total_records': {
                'security': len(self.security_logs),
                'performance': len(self.performance_data),
                'architecture': len(self.architecture_data),
                'cost': len(self.cost_data),
                'scaling': len(self.scaling_events)
            }
        }
        
        with open(f"{output_dir}/simulation_summary.json", 'w') as f:
            json.dump(summary, f, indent=2)
        
        print(f"\n✓ Summary saved: {output_dir}/simulation_summary.json")
        print(f"\nDATA EXPORT COMPLETE!")

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*80)
    print(" RUNNING HYBRID CLOUD SIMULATION")
    print(" Group Project: Enhancing Educational Service Delivery")
    print("="*80)
    
    # CREATE THE UNIFIED MODEL
    print("\nStep 1: Creating the Hybrid Cloud Model (THE shared artefact)...")
    model = HybridCloudModel(security_level="intermediate")
    
    # RUN SIMULATION
    print("\nStep 2: Running Simulation Scenarios...")
    
    # You can choose which scenarios to run:
    scenarios_to_run = [
        WorkloadScenario.MODERATE_DEMAND,  # 24-hour regular period
        WorkloadScenario.PEAK_DEMAND       # 8-hour peak period
    ]
    
    for scenario in scenarios_to_run:
        model.simulate_scenario(scenario, verbose=True)
    
    # EXPORT DATA FOR ALL FOUR RESEARCHERS
    print("\nStep 3: Exporting Data for All Four Researchers...")
    model.export_data(output_dir="GROUP_PROJECT_DATA")
    
    print("\n" + "="*80)
    print(" SIMULATION COMPLETE!")
    print(" All four team members can now analyze their respective datasets")
    print("="*80)
    print("\nGenerated files in 'GROUP_PROJECT_DATA' folder:")
    print("  → ADEYEMI_security_data.csv (Security & Compliance)")
    print("  → TEMITAYO_performance_data.csv (Performance & Optimization)")
    print("  → ESTHER_architecture_data.csv (Architecture & Design)")
    print("  → DAVID_cost_data.csv (Cost Efficiency)")
    print("  → DAVID_scaling_events.csv (Scalability)")
    print("\n" + "="*80)
