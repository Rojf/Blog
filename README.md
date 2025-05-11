# Blog

A blog based on a Clean architecture.

❗️ **Note **: This project is under development and may be unstable or deficient in functionality.

---

## 🤝 Contributing

Want to help? Contributions are welcome!  
Check out the [Discussions](https://github.com/Rojf/Blog/discussions) and [Project Roadmap](https://github.com/Rojf/Blog/projects) to get started.

---

## 🛠️ Tech Stack

- **Languages**:
  - Python `3.12`

- **Frameworks**:
  - Django `5.0.6`
  - Django REST framework `3.15.1`

- **Databases & Storage**:
  - PostgreSQL `17.2`
  - Redis `7.4`

- **Messaging & Tasks**:
  - Celery `5.x` *(add exact version)*

- **API Gateway & Networking**:
  - NGINX

- **Dev Tools**:
  - Docker
  - Poetry
  - Make
  - Pytest

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Rojf/Blog
cd Blog
```


---

### 2. Run Locally and Stop

⚠️ If `make local-down` fails due to `kill` permissions, try running with administrator rights:

```bash
# Install dependencies
make local-build

# Start services
make local-up

# Stop services
make local-down
```


---

### 3. Run Fully in Docker and Stop

```bash
# start app in docker
make docker-up

# Stop app in docker
make docker-down
```


---


### 📚 Documentation

| Service         | Documentation Path            | Description                  |
| --------------- | ----------------------------- | ---------------------------- |
|                 |                               |                              |
|                 |                               |                              |
|                 |                               |                              |


To explore APIs, expected request/response formats, and workflows, check the relevant `README.md` inside each subdirectory.

---

## 🧭 Product Roadmap

[Discussions](https://github.com/Rojf/Blog/discussions) | [Kanban Board](https://github.com/Rojf/Blog/projects)

✅ Completed – Deployed and functional  
🔄 In Progress – Actively being developed  
📅 Planned – Scheduled for the future

| Status | Feature      | Release  |
| ------ | ------------ | -------- |
| ✅      | Basic setup  | `v0.1.0` |
| 🔄     | Auth service | `v0.2.0` |
| 📅     | Admin panel  | `v0.3.0` |

