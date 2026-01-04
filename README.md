# Secure DevOps CI/CD with SonarCloud

This project demonstrates the implementation of **Secure DevOps (DevSecOps)** practices by integrating **SonarCloud (SonarQube)** security scanning into a **CI/CD pipeline using GitHub Actions**.

The goal is to automatically detect security issues early in the development lifecycle (Shift-Left Security).

---

## 🚀 Tech Stack

- Python
- GitHub Actions (CI/CD)
- SonarCloud (Static Code Analysis / SAST)
- YAML (Pipeline configuration)

---

## 📌 Project Objective

- Integrate security scanning into CI/CD
- Identify vulnerabilities in source code
- Enforce Quality Gates to block insecure code
- Demonstrate Secure DevOps best practices

---

## ⚙️ CI/CD Pipeline Workflow

1. Code is pushed to the GitHub repository
2. GitHub Actions triggers the CI pipeline
3. SonarCloud scans the Python codebase
4. Security issues and hotspots are detected
5. Quality Gate evaluates the security status
6. Pipeline fails if security conditions are not met

---

## 🔐 Security Analysis

- SonarCloud detected **Security Hotspots** in the Python application
- Example risk: **Unsanitized user input leading to SQL Injection**
- Quality Gate failed due to unreviewed security hotspots
- Manual security review was required (human-in-the-loop security)

---

## 📊 Quality Gate Result

- ❌ Quality Gate: Failed
- ❌ Reason: Security hotspots not reviewed (Required: 100%)

This behavior confirms that the security enforcement is working as expected.

---

## 🛡️ Key Learnings

- Implemented Shift-Left Security
- Integrated static security analysis into CI/CD
- Understood Quality Gates and Security Hotspots
- Learned how CI pipelines prevent vulnerable code from deployment

---

## 📎 Conclusion

This project successfully demonstrates how Secure DevOps practices can be applied by integrating automated security scanning into a CI/CD pipeline, ensuring early detection and prevention of security vulnerabilities.

---

## 👤 Author

**Rishi Kesh V**  
Secure DevOps Internship Task
