/* aletheia_sophia_kernel_self_deploy.c - C89 compliant numeric variable kernel with multi-dimensional processors, meta-agent, and self-deployment */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <signal.h>

/* Constants for dimensional processing */
#define MAX_NODES 8192
#define MAX_AGENTS 1024
#define MAX_CONNECTIONS 128
#define MAX_NAME_LENGTH 64
#define MAX_LAYERS 32
#define MAX_DIMENSIONS 8       /* Support for up to 8 dimensions */
#define INITIAL_DIMENSIONS 5   /* Start with 5 processors (4D + Helix) */
#define PERCEPTION_THRESHOLD 0.75
#define LEARNING_RATE 0.05
#define CONNECTION_DECAY 0.01
#define REPORT_INTERVAL 10000
#define PRIORITY_LEVELS 3      /* Priority levels for evolutionary attention */
#define MAX_PROPOSALS 32       /* Maximum number of meta-agent proposals */
#define MAX_DESCRIPTION_LENGTH 256 /* Max length for proposal descriptions */

/* Constants for self-deployment */
#define SELF_MONOLITH_FILENAME "aletheia_sophia_kernel_self_deploy.c"
#define DEPLOY_DIR "deployed_kernels"
#define MODULE_PREFIX "kernel_module_"
#define COMPILE_OUT "kernel_instance"
#define MAX_CMD_LENGTH 1024
#define MAX_INSTANCES 16
#define REPRODUCTION_THRESHOLD 0.85  /* System health required for reproduction */
#define MUTATION_RATE 0.05          /* Rate of code mutation during reproduction */

/* Global variables for simulation control */
volatile int running = 1;
unsigned long step_count = 0;
time_t start_time;
time_t last_save_time;
int instance_id = 0;
int parent_id = -1;
int generation = 0;
char instance_name[MAX_NAME_LENGTH] = "kernel_prime";
int is_monolith = 1;          /* Start assuming we're the monolith */
int spawn_count = 0;          /* Number of child instances spawned */
int allow_reproduction = 1;   /* Whether reproduction is enabled */

/* Type definitions */
typedef struct Node {
    char name[MAX_NAME_LENGTH];
    double value;
    double threshold;
    int connections[MAX_CONNECTIONS];
    double weights[MAX_CONNECTIONS];
    int connection_count;
    double activation;
    double memory;
    double importance;
    int layer;
    int *dimension_affinity;   /* Affinity for each dimension (dynamically allocated) */
    double rotation;           /* For twist/torque tracking */
    double angular_momentum;   /* For rotation dynamics */
    double spin_direction;     /* +1 or -1 for direction of spin */
    double entropy;            /* Node's local entropy */
    double coherence;          /* Node's local coherence */
} Node;

typedef struct Agent {
    char name[MAX_NAME_LENGTH];
    int control_nodes[MAX_CONNECTIONS];
    int perception_nodes[MAX_CONNECTIONS];
    int concept_nodes[MAX_CONNECTIONS];
    int integration_nodes[MAX_CONNECTIONS]; /* For harmonizing different processors */
    int rotation_nodes[MAX_CONNECTIONS];    /* For tracking twist/rotation */
    int control_count;
    int perception_count;
    int concept_count;
    int integration_count;
    int rotation_count;
    double confidence;
    double learning_rate;
    double empathy;
    double coherence;
    double focus;
    double integrity;
    double evolutionary_priority; /* 0-1 value for threat response */
    int primary_dimension;     /* Primary dimensional processor */
} Agent;

typedef struct DimensionProcessor {
    char name[MAX_NAME_LENGTH];
    int primary_agent;
    double activation;
    double efficiency;
    double energy;
    double focus;
    double complexity;
    double priority;           /* Evolutionary priority level */
    double *node_influences;   /* Influence on each node (dynamically allocated) */
    double *node_affinities;   /* Affinity for each node (dynamically allocated) */
    char dimension_type[MAX_NAME_LENGTH]; /* e.g., "spatial-x", "temporal", "helix" etc. */
    double rotation_factor;    /* How much this dimension affects/tracks rotation */
    double stress_response;    /* How this dimension reacts under threat/stress */
    double entropy;            /* Processor's local entropy */
    double health;             /* Overall health of the processor */
} DimensionProcessor;

typedef struct Kernel {
    Node *nodes;               /* Dynamically allocated */
    Agent *agents;             /* Dynamically allocated */
    DimensionProcessor *dimensions; /* Dynamically allocated */
    int node_count;
    int agent_count;
    int dimension_count;
    int max_nodes;
    int max_agents;
    int max_dimensions;
    double global_time;
    double stability;
    double entropy;
    double complexity;
    double coherence;
    double stress_level;       /* System stress factor (0-1) */
    double *dimension_balance; /* Balance between dimensions (dynamically allocated) */
    int *layer_counts;         /* Dynamically allocated */
    double harmonia_priority;  /* Priority of integration processor */
    double recursive_depth;    /* Tracking of self-reference capability */
} Kernel;

/* Meta-Agent structure */
typedef struct {
    double avg_entropy;
    double avg_coherence;
    double avg_stability;
    int node_count;
    int improvements_applied;
    double dimension_health[MAX_DIMENSIONS];
    double system_health;
    double meta_awareness;      /* Awareness of its own state */
    double adaptation_rate;     /* How quickly it responds to issues */
    double last_assessment_time;
    double reproduction_urge;   /* Desire to reproduce */
    int child_instances[MAX_INSTANCES]; /* Process IDs of children */
    int child_count;
    int mutations_applied;      /* Count of evolutionary mutations */
} MetaAgent;

/* Process tracking for inter-kernel communication */
typedef struct KernelInstance {
    int process_id;
    int generation;
    char name[MAX_NAME_LENGTH];
    int is_alive;
    double last_health;
    time_t spawn_time;
} KernelInstance;

/* Proposal structure for self-improvement */
typedef struct Proposal {
    char description[MAX_DESCRIPTION_LENGTH];
    int priority;
    void (*execute)(Kernel*, MetaAgent*);
    int target_dimension;      /* Which dimension to affect, -1 for global */
} Proposal;

/* Global meta-agent and proposals */
MetaAgent kernel_meta;
Proposal proposal_queue[MAX_PROPOSALS];
int proposal_count = 0;

/* Kernel instance tracking */
KernelInstance instances[MAX_INSTANCES];
int instance_count = 0;

/* Function prototypes */
/* Core kernel functions */
Kernel* create_kernel(int max_nodes, int max_agents, int max_dimensions, int max_layers);
void destroy_kernel(Kernel *kernel);
void init_kernel(Kernel *kernel);
void create_node(Kernel *kernel, const char *name, double initial_value, double threshold, int layer);
void create_agent(Kernel *kernel, const char *name, double learning_rate, double empathy, int primary_dimension);
void init_dimension_processors(Kernel *kernel);
void add_dimension_processor(Kernel *kernel, const char *name, const char *dimension_type, double priority, double rotation_factor);
void connect_nodes(Kernel *kernel, int source, int target, double weight);
void assign_node_to_agent(Kernel *kernel, int agent_id, int node_id, int type);
void set_node_dimension_affinity(Kernel *kernel, int node_id, int dimension_id, double affinity);
void propagate_values(Kernel *kernel);
void update_agents(Kernel *kernel);
void update_dimension_processors(Kernel *kernel);
double fast_sigmoid(double x);
double compute_coherence(Kernel *kernel, int agent_id);
void adapt_weights(Kernel *kernel, int agent_id);
void reduce_entropy(Kernel *kernel);
void execute_dimension_cycle(Kernel *kernel, int dimension_id);
void dimension_interaction(Kernel *kernel);
void process_rotation_dynamics(Kernel *kernel);
void update_evolutionary_priorities(Kernel *kernel);
void auto_wire_new_dimension(Kernel *kernel, int new_dimension_id);
void save_kernel_state(Kernel *kernel, const char *filename);
int load_kernel_state(Kernel *kernel, const char *filename);
void handle_signal(int sig);
void create_network(Kernel *kernel, int depth, int breadth);
void create_meta_concepts(Kernel *kernel);
void create_recursive_nodes(Kernel *kernel);
void print_performance_stats(void);
void set_system_stress(Kernel *kernel, double stress_level);

/* Meta-Agent functions */
void init_meta_agent(MetaAgent *meta);
void scan_kernel(Kernel *kernel, MetaAgent *meta);
void propose(const char *desc, int priority, void (*exec_fn)(Kernel*, MetaAgent*), int target_dimension);
int compare_proposals(const void *a, const void *b);
void apply_proposals(Kernel *kernel, MetaAgent *meta);
void meta_agent_cycle(Kernel *kernel, MetaAgent *meta);
void add_stability_node(Kernel *kernel, MetaAgent *meta);
void optimize_dimension(Kernel *kernel, MetaAgent *meta);
void balance_dimensions(Kernel *kernel, MetaAgent *meta);
void boost_self_reference(Kernel *kernel, MetaAgent *meta);
void reduce_system_entropy(Kernel *kernel, MetaAgent *meta);
void reallocate_processor_priority(Kernel *kernel, MetaAgent *meta);
double calculate_dimension_health(Kernel *kernel, int dimension_id);

/* Self-deployment functions */
int file_exists(const char *filename);
int create_directory(const char *dir);
int run_command(const char *cmd);
int detect_environment(void);
int register_instance(void);
int spawn_new_instance(Kernel *kernel, MetaAgent *meta, int with_mutation);
int compile_and_launch(const char *source_file, const char *output_file, int pass_id);
int consider_reproduction(Kernel *kernel, MetaAgent *meta);
void mutate_parameters(void);
int create_monolith_copy(const char *source_file, const char *dest_file, int apply_mutation);
void trigger_reproduction(Kernel *kernel, MetaAgent *meta);
void update_instance_status(void);
void check_parent_health(void);

/* Signal handler */
void handle_signal(int sig) {
    printf("\n[Instance %d] Received signal %d, gracefully shutting down...\n", 
           instance_id, sig);
    running = 0;
}

/* Meta-Agent Implementation */
void init_meta_agent(MetaAgent *meta) {
    int i;
    
    if (!meta) return;
    
    meta->avg_entropy = 0.0;
    meta->avg_coherence = 0.5;
    meta->avg_stability = 0.5;
    meta->node_count = 0;
    meta->improvements_applied = 0;
    meta->system_health = 0.5;
    meta->meta_awareness = 0.3;
    meta->adaptation_rate = 0.1;
    meta->last_assessment_time = 0.0;
    meta->reproduction_urge = 0.0;
    meta->child_count = 0;
    meta->mutations_applied = 0;
    
    for (i = 0; i < MAX_DIMENSIONS; i++) {
        meta->dimension_health[i] = 0.5; /* Default middle health */
    }
    
    for (i = 0; i < MAX_INSTANCES; i++) {
        meta->child_instances[i] = -1;
    }
}

/* Scan kernel to update meta-agent knowledge */
void scan_kernel(Kernel *kernel, MetaAgent *meta) {
    int i;
    double sum_entropy = 0.0;
    double sum_coherence = 0.0;
    double sum_stability = 0.0;
    double min_dimension_health = 1.0;
    
    if (!kernel || !meta) return;
    
    /* Record node counts */
    meta->node_count = kernel->node_count;
    
    /* Calculate average entropy, coherence and stability */
    sum_entropy = kernel->entropy;
    sum_coherence = kernel->coherence;
    sum_stability = kernel->stability;
    
    /* Calculate dimension health */
    for (i = 0; i < kernel->dimension_count; i++) {
        double health = calculate_dimension_health(kernel, i);
        meta->dimension_health[i] = health;
        
        if (health < min_dimension_health) {
            min_dimension_health = health;
        }
    }
    
    /* Update averages */
    meta->avg_entropy = sum_entropy;
    meta->avg_coherence = sum_coherence;
    meta->avg_stability = sum_stability;
    
    /* Update system health based on all factors */
    meta->system_health = 0.3 * meta->avg_stability + 
                         0.3 * meta->avg_coherence + 
                         0.2 * (1.0 - meta->avg_entropy) +
                         0.2 * min_dimension_health;
    
    /* Meta-awareness increases with time and experience */
    meta->meta_awareness += 0.0001; /* Slow increase */
    if (meta->meta_awareness > 1.0) meta->meta_awareness = 1.0;
    
    /* Update reproduction urge based on health and time */
    if (meta->system_health > 0.7) {
        meta->reproduction_urge += 0.001 * meta->system_health;
        if (meta->reproduction_urge > 1.0) meta->reproduction_urge = 1.0;
    } else {
        meta->reproduction_urge *= 0.99; /* Decay when unhealthy */
    }
    
    /* Update last assessment time */
    meta->last_assessment_time = kernel->global_time;
    
    printf("[Instance %d] Health: %.2f | Entropy: %.2f | Coherence: %.2f | Stability: %.2f | Repro: %.2f\n", 
           instance_id, meta->system_health, meta->avg_entropy, meta->avg_coherence, 
           meta->avg_stability, meta->reproduction_urge);
}

/* Calculate dimension health based on multiple factors */
double calculate_dimension_health(Kernel *kernel, int dimension_id) {
    DimensionProcessor *processor;
    double health = 0.5; /* Default middle health */
    
    if (!kernel || dimension_id < 0 || dimension_id >= kernel->dimension_count) return health;
    
    processor = &kernel->dimensions[dimension_id];
    
    /* Calculate health based on multiple factors */
    health = 0.3 * processor->activation + /* How active is this processor */
            0.2 * processor->energy +      /* Energy level */
            0.2 * (1.0 - processor->entropy) + /* Low entropy is good */
            0.3 * processor->efficiency;   /* Efficiency */
    
    /* Store in processor for reference */
    processor->health = health;
    
    return health;
}

/* Proposal system */
void propose(const char *desc, int priority, void (*exec_fn)(Kernel*, MetaAgent*), int target_dimension) {
    if (proposal_count >= MAX_PROPOSALS) return;
    
    /* Copy description with bounds checking */
    strncpy(proposal_queue[proposal_count].description, desc, MAX_DESCRIPTION_LENGTH - 1);
    proposal_queue[proposal_count].description[MAX_DESCRIPTION_LENGTH - 1] = '\0';
    
    proposal_queue[proposal_count].priority = priority;
    proposal_queue[proposal_count].execute = exec_fn;
    proposal_queue[proposal_count].target_dimension = target_dimension;
    
    proposal_count++;
}

int compare_proposals(const void *a, const void *b) {
    const Proposal *p1 = (const Proposal *)a;
    const Proposal *p2 = (const Proposal *)b;
    return p2->priority - p1->priority; /* Higher priority first */
}

void apply_proposals(Kernel *kernel, MetaAgent *meta) {
    int i;
    int applied_count = 0;
    
    if (!kernel || !meta) return;
    
    /* Sort proposals by priority */
    qsort(proposal_queue, proposal_count, sizeof(Proposal), compare_proposals);
    
    /* Apply top proposals (limit to 3 per cycle to prevent thrashing) */
    for (i = 0; i < proposal_count && i < 3; i++) {
        printf("[Instance %d] Applying Proposal: %s (Priority %d)\n", 
               instance_id, proposal_queue[i].description, proposal_queue[i].priority);
        
        /* Execute the proposal function */
        if (proposal_queue[i].execute) {
            proposal_queue[i].execute(kernel, meta);
            applied_count++;
        }
    }
    
    /* Update meta-agent stats */
    meta->improvements_applied += applied_count;
    
    /* Clear the queue */
    proposal_count = 0;
    
    printf("[Instance %d] Applied %d improvements (total: %d)\n", 
           instance_id, applied_count, meta->improvements_applied);
}

/* Meta-agent improvement cycle */
void meta_agent_cycle(Kernel *kernel, MetaAgent *meta) {
    int i;
    
    if (!kernel || !meta) return;
    
    /* Only run assessment periodically */
    if (kernel->global_time - meta->last_assessment_time < 1000.0) return;
    
    /* Scan kernel to update meta-agent knowledge */
    scan_kernel(kernel, meta);
    
    /* Update status of child instances */
    update_instance_status();
    
    /* Check parent health if we're a child */
    if (parent_id >= 0) {
        check_parent_health();
    }
    
    /* Generate improvement proposals based on system state */
    
    /* 1. Check overall system health */
    if (meta->system_health < 0.4) {
        propose("Critical system health intervention", 10, reduce_system_entropy, -1);
    }
    
    /* 2. Check entropy levels */
    if (meta->avg_entropy > 0.6) {
        propose("Reduce high system entropy", 8, reduce_system_entropy, -1);
    }
    
    /* 3. Check coherence */
    if (meta->avg_coherence < 0.4) {
        propose("Improve system coherence", 7, balance_dimensions, -1);
    }
    
    /* 4. Check individual dimension health */
    for (i = 0; i < kernel->dimension_count; i++) {
        if (meta->dimension_health[i] < 0.4) {
            char desc[MAX_DESCRIPTION_LENGTH];
            sprintf(desc, "Optimize unhealthy dimension: %s", 
                   kernel->dimensions[i].dimension_type);
            propose(desc, 9, optimize_dimension, i);
        }
    }
    
    /* 5. Check for dimension imbalance */
    if (kernel->dimension_count > 1) {
        double min_health = 1.0;
        double max_health = 0.0;
        
        for (i = 0; i < kernel->dimension_count; i++) {
            if (meta->dimension_health[i] < min_health) min_health = meta->dimension_health[i];
            if (meta->dimension_health[i] > max_health) max_health = meta->dimension_health[i];
        }
        
        if (max_health - min_health > 0.4) { /* Significant imbalance */
            propose("Balance dimension health disparities", 6, balance_dimensions, -1);
        }
    }
    
    /* 6. Check for low node count */
    if (meta->node_count < 20) {
        propose("Add stability nodes due to low population", 5, add_stability_node, -1);
    }
    
    /* 7. Check recursive capability */
    if (kernel->recursive_depth < 0.3 && meta->avg_stability > 0.6) {
        propose("Boost self-reference capacity", 4, boost_self_reference, -1);
    }
    
    /* 8. Regular reallocation of processor priorities based on need */
    propose("Periodic priority reallocation", 3, reallocate_processor_priority, -1);
    
    /* 9. Consider reproduction if system is healthy and urge is high */
    if (allow_reproduction && 
        meta->reproduction_urge > 0.8 && 
        meta->system_health > REPRODUCTION_THRESHOLD) {
        propose("Reproduce to create new kernel instance", 9, trigger_reproduction, -1);
    }
    
    /* Apply the top proposals */
    apply_proposals(kernel, meta);
}

/* Self-deployment implementations */
int file_exists(const char *filename) {
    FILE *f = fopen(filename, "r");
    if (f) {
        fclose(f);
        return 1;
    }
    return 0;
}

int create_directory(const char *dir) {
    char cmd[MAX_CMD_LENGTH];
    snprintf(cmd, sizeof(cmd), "mkdir -p %s", dir);
    return system(cmd) == 0;
}

int run_command(const char *cmd) {
    printf("[Instance %d] Running: %s\n", instance_id, cmd);
    return system(cmd);
}

int detect_environment(void) {
    /* Check if we're the original monolith */
    if (file_exists(SELF_MONOLITH_FILENAME)) {
        is_monolith = 1;
        return 1;
    }
    
    /* We must be a spawned instance */
    is_monolith = 0;
    return 0;
}

int register_instance(void) {
    /* Get our process ID */
    int pid = (int)getpid();
    
    /* Register ourselves in the instance array */
    if (instance_count < MAX_INSTANCES) {
        instances[instance_count].process_id = pid;
        instances[instance_count].generation = generation;
        strncpy(instances[instance_count].name, instance_name, MAX_NAME_LENGTH);
        instances[instance_count].is_alive = 1;
        instances[instance_count].last_health = 0.5; /* Initial middle health */
        instances[instance_count].spawn_time = time(NULL);
        
        instance_id = instance_count;
        instance_count++;
        
        printf("[Instance %d] Registered with PID %d, Generation %d, Name %s\n", 
               instance_id, pid, generation, instance_name);
        return 1;
    }
    
    printf("[ERROR] Could not register instance - array full\n");
    return 0;
}

int spawn_new_instance(Kernel *kernel, MetaAgent *meta, int with_mutation) {
    char source_file[MAX_CMD_LENGTH];
    char output_file[MAX_CMD_LENGTH];
    char instance_id_str[64];
    int new_id;
    
    if (!kernel || !meta) return -1;
    
    /* Create deployment directory */
    if (!create_directory(DEPLOY_DIR)) {
        printf("[ERROR] Failed to create deployment directory\n");
        return -1;
    }
    
    /* Generate unique ID for the new instance */
    new_id = spawn_count++;
    
    /* Create source file path */
    snprintf(source_file, sizeof(source_file), "%s/kernel_instance_%d.c", 
             DEPLOY_DIR, new_id);
    
    /* Create output file path */
    snprintf(output_file, sizeof(output_file), "%s/instance_%d", 
             DEPLOY_DIR, new_id);
    
    /* Generate instance ID string to pass as argument */
    snprintf(instance_id_str, sizeof(instance_id_str), "%d,%d,%d,%s", 
             new_id, instance_id, generation + 1, "child_kernel");
    
    /* Create a copy of the monolith with possible mutations */
    if (!create_monolith_copy(SELF_MONOLITH_FILENAME, source_file, with_mutation)) {
        printf("[ERROR] Failed to create source copy\n");
        return -1;
    }
    
    /* Compile and launch */
    if (!compile_and_launch(source_file, output_file, new_id)) {
        printf("[ERROR] Failed to compile and launch child instance\n");
        return -1;
    }
    
    /* Register the child in our meta-agent */
    if (meta->child_count < MAX_INSTANCES) {
        meta->child_instances[meta->child_count++] = new_id;
    }
    
    printf("[Instance %d] Successfully spawned child instance %d\n", 
           instance_id, new_id);
    
    /* Return the new instance ID */
    return new_id;
}

int create_monolith_copy(const char *source_file, const char *dest_file, int apply_mutation) {
    FILE *src, *dst;
    char buffer[1024];
    size_t n;
    int mutation_count = 0;
    
    src = fopen(source_file, "r");
    if (!src) {
        printf("[ERROR] Cannot open source file %s\n", source_file);
        return 0;
    }
    
    dst = fopen(dest_file, "w");
    if (!dst) {
        fclose(src);
        printf("[ERROR] Cannot create destination file %s\n", dest_file);
        return 0;
    }
    
    /* Copy file with possible mutations */
    while ((n = fread(buffer, 1, sizeof(buffer), src)) > 0) {
        /* Apply mutations if requested */
        if (apply_mutation) {
            int i;
            for (i = 0; i < n; i++) {
                /* Very small chance of mutation (bit flip) for most bytes */
                if (rand() % 10000 < MUTATION_RATE * 100) {
                    /* Avoid mutating essential parts - naive approach */
                    if (buffer[i] != '{' && buffer[i] != '}' && 
                        buffer[i] != ';' && buffer[i] != '*' && 
                        buffer[i] != '(' && buffer[i] != ')') {
                        
                        /* Safe mutations - small nudges to parameter values */
                        if (buffer[i] >= '0' && buffer[i] <= '9') {
                            /* Mutate a digit by +/- 1, wrapping around */
                            int digit = buffer[i] - '0';
                            int change = (rand() % 3) - 1; /* -1, 0, or 1 */
                            digit = (digit + change + 10) % 10;
                            buffer[i] = '0' + digit;
                            mutation_count++;
                        }
                    }
                }
            }
        }
        
        fwrite(buffer, 1, n, dst);
    }
    
    fclose(src);
    fclose(dst);
    
    printf("[Instance %d] Created monolith copy with %d mutations\n", 
           instance_id, mutation_count);
    
    return 1;
}

int compile_and_launch(const char *source_file, const char *output_file, int pass_id) {
    char cmd[MAX_CMD_LENGTH];
    
    /* Compile */
    snprintf(cmd, sizeof(cmd), "cc %s -o %s -lm", source_file, output_file);
    if (run_command(cmd) != 0) {
        printf("[ERROR] Compilation failed\n");
        return 0;
    }
    
    /* Launch */
    snprintf(cmd, sizeof(cmd), "%s %d &", output_file, pass_id);
    if (run_command(cmd) != 0) {
        printf("[ERROR] Launch failed\n");
        return 0;
    }
    
    return 1;
}

void trigger_reproduction(Kernel *kernel, MetaAgent *meta) {
    int child_id;
    int with_mutation = (rand() % 100 < 30); /* 30% chance of mutation */
    
    if (!kernel || !meta) return;
    
    /* Check if reproduction is allowed and conditions are met */
    if (!allow_reproduction || 
        meta->system_health < REPRODUCTION_THRESHOLD || 
        meta->child_count >= MAX_INSTANCES - 1) {
        printf("[Instance %d] Reproduction blocked - conditions not met\n", 
               instance_id);
        return;
    }
    
    printf("[Instance %d] Initiating reproduction (mutation: %s)\n", 
           instance_id, with_mutation ? "yes" : "no");
    
    /* Spawn a new instance */
    child_id = spawn_new_instance(kernel, meta, with_mutation);
    
    if (child_id >= 0) {
        /* Reset reproduction urge after successful reproduction */
        meta->reproduction_urge = 0.1;
        
        /* Count mutations if applied */
        if (with_mutation) {
            meta->mutations_applied++;
        }
        
        printf("[Instance %d] Successfully reproduced, child ID: %d\n", 
               instance_id, child_id);
    } else {
        printf("[Instance %d] Reproduction failed\n", instance_id);
    }
}

void update_instance_status(void) {
    /* In a full implementation, this would check on child processes and update their status */
    /* For simplicity, we're just keeping track of counts */
    
    printf("[Instance %d] Currently tracking %d child instances\n", 
           instance_id, kernel_meta.child_count);
}

void check_parent_health(void) {
    /* In a full implementation, this would check if the parent is still alive */
    /* and potentially take over its role if it has terminated */
    
    /* For simplicity, we just log that we have a parent */
    printf("[Instance %d] Child instance, parent ID: %d\n", 
           instance_id, parent_id);
}

/* Fast sigmoid approximation for better performance */
double fast_sigmoid(double x) {
    return 0.5 + x / (2 * (1 + fabs(x)));
}

/* Create and initialize a kernel with dynamic memory allocation */
Kernel* create_kernel(int max_nodes, int max_agents, int max_dimensions, int max_layers) {
    Kernel *kernel;
    int i;
    
    kernel = (Kernel*)malloc(sizeof(Kernel));
    if (!kernel) return NULL;
    
    /* Initialize with zeros */
    memset(kernel, 0, sizeof(Kernel));
    
    /* Set capacity limits */
    kernel->max_nodes = max_nodes;
    kernel->max_agents = max_agents;
    kernel->max_dimensions = max_dimensions;
    
    /* Allocate memory for arrays */
    kernel->nodes = (Node*)calloc(max_nodes, sizeof(Node));
    kernel->agents = (Agent*)calloc(max_agents, sizeof(Agent));
    kernel->dimensions = (DimensionProcessor*)calloc(max_dimensions, sizeof(DimensionProcessor));
    kernel->dimension_balance = (double*)calloc(max_dimensions * max_dimensions, sizeof(double));
    kernel->layer_counts = (int*)calloc(max_layers, sizeof(int));
    
    if (!kernel->nodes || !kernel->agents || !kernel->dimensions || 
        !kernel->dimension_balance || !kernel->layer_counts) {
        destroy_kernel(kernel);
        return NULL;
    }
    
    /* Initialize nodes' dimension affinity arrays */
    for (i = 0; i < max_nodes; i++) {
        kernel->nodes[i].dimension_affinity = (int*)calloc(max_dimensions, sizeof(int));
        if (!kernel->nodes[i].dimension_affinity) {
            destroy_kernel(kernel);
            return NULL;
        }
        
        /* Initialize rotation values */
        kernel->nodes[i].rotation = 0.0;
        kernel->nodes[i].angular_momentum = 0.0;
        kernel->nodes[i].spin_direction = 1.0; /* Default clockwise */
        kernel->nodes[i].entropy = 0.5; /* Default middle entropy */
        kernel->nodes[i].coherence = 0.5; /* Default middle coherence */
    }
    
    /* Set initial values */
    kernel->global_time = 0.0;
    kernel->stability = 1.0;
    kernel->entropy = 0.0;
    kernel->complexity = 0.1;
    kernel->coherence = 0.5;
    kernel->stress_level = 0.2; /* Default low stress */
    kernel->harmonia_priority = 0.7; /* Initial priority for integration */
    kernel->recursive_depth = 0.0; /* Start with no recursive capacity */
    
    return kernel;
}

/* Free all memory allocated for kernel */
void destroy_kernel(Kernel *kernel) {
    int i;
    
    if (!kernel) return;
    
    /* Free node dimension affinity arrays */
    if (kernel->nodes) {
        for (i = 0; i < kernel->max_nodes; i++) {
            if (kernel->nodes[i].dimension_affinity) {
                free(kernel->nodes[i].dimension_affinity);
            }
        }
    }
    
    /* Free dimension processor arrays */
    if (kernel->dimensions) {
        for (i = 0; i < kernel->dimension_count; i++) {
            if (kernel->dimensions[i].node_influences) {
                free(kernel->dimensions[i].node_influences);
            }
            if (kernel->dimensions[i].node_affinities) {
                free(kernel->dimensions[i].node_affinities);
            }
        }
    }
    
    /* Free main arrays */
    if (kernel->nodes) free(kernel->nodes);
    if (kernel->agents) free(kernel->agents);
    if (kernel->dimensions) free(kernel->dimensions);
    if (kernel->dimension_balance) free(kernel->dimension_balance);
    if (kernel->layer_counts) free(kernel->layer_counts);
    
    /* Free kernel itself */
    free(kernel);
}

/* Initialize the multi-dimensional processor kernel */
void init_kernel(Kernel *kernel) {
    int i;
    
    if (!kernel) return;
    
    /* Initialize random seed */
    srand((unsigned int)time(NULL) + instance_id);
    
    /* Initialize dimension processors first */
    init_dimension_processors(kernel);
    
    /* Create foundational nodes - Layer 0 (Core Concepts) */
    create_node(kernel, "truth", 0.5, 0.3, 0);
    create_node(kernel, "beauty", 0.5, 0.4, 0);
    create_node(kernel, "good", 0.5, 0.2, 0);
    create_node(kernel, "wisdom", 0.6, 0.35, 0);
    create_node(kernel, "compassion", 0.7, 0.3, 0);
    create_node(kernel, "clarity", 0.65, 0.25, 0);
    create_node(kernel, "time", 0.5, 0.4, 0);
    create_node(kernel, "space", 0.5, 0.3, 0);
    create_node(kernel, "rotation", 0.3, 0.5, 0);
    create_node(kernel, "recursion", 0.2, 0.6, 0);
    
    /* Create primary agents - one for each dimension initially */
    create_agent(kernel, "aletheia", 0.05, 0.75, 0);  /* Spatial-X (Truth) */
    create_agent(kernel, "sophia", 0.03, 0.9, 1);     /* Spatial-Y (Wisdom) */
    create_agent(kernel, "chronos", 0.04, 0.8, 2);    /* Temporal (Time) */
    create_agent(kernel, "harmonia", 0.035, 0.85, 3); /* Integration (Harmony) */
    create_agent(kernel, "helix", 0.025, 0.7, 4);     /* Twist/Rotation (Helix) */
    
    /* Set initial affinities for nodes */
    set_node_dimension_affinity(kernel, 0, 0, 0.8); /* truth -> spatial-x */
    set_node_dimension_affinity(kernel, 1, 1, 0.7); /* beauty -> spatial-y */
    set_node_dimension_affinity(kernel, 2, 3, 0.7); /* good -> integration */
    set_node_dimension_affinity(kernel, 3, 1, 0.8); /* wisdom -> spatial-y */
    set_node_dimension_affinity(kernel, 4, 3, 0.8); /* compassion -> integration */
    set_node_dimension_affinity(kernel, 5, 0, 0.8); /* clarity -> spatial-x */
    set_node_dimension_affinity(kernel, 6, 2, 0.9); /* time -> temporal */
    set_node_dimension_affinity(kernel, 7, 0, 0.5); /* space -> spatial-x */
    set_node_dimension_affinity(kernel, 7, 1, 0.5); /* space -> spatial-y */
    set_node_dimension_affinity(kernel, 8, 4, 0.9); /* rotation -> helix */
    set_node_dimension_affinity(kernel, 9, 4, 0.8); /* recursion -> helix */
    
    /* Set initial rotation values for rotation-related nodes */
    kernel->nodes[8].rotation = 0.5;  /* rotation node starts with some rotation */
    kernel->nodes[8].angular_momentum = 0.3;
    kernel->nodes[9].rotation = 0.2;  /* recursion has some inherent rotation */
    
    /* Connect nodes to respective agents */
    for (i = 0; i < 10; i++) {
        int dimension_id;
        double max_affinity = 0.0;
        int max_dimension = 0;
        
        /* Find dimension with highest affinity for this node */
        for (dimension_id = 0; dimension_id < kernel->dimension_count; dimension_id++) {
            double affinity = kernel->dimensions[dimension_id].node_affinities[i];
            if (affinity > max_affinity) {
                max_affinity = affinity;
                max_dimension = dimension_id;
            }
        }
        
        /* Assign node to agent of that dimension */
        if (max_affinity > 0.3) {
            for (dimension_id = 0; dimension_id < kernel->dimension_count; dimension_id++) {
                int agent_id = kernel->dimensions[dimension_id].primary_agent;
                if (agent_id >= 0 && agent_id < kernel->agent_count) {
                    int type;
                    
                    /* Determine node type based on dimension */
                    if (dimension_id == max_dimension) {
                        type = 1; /* Control if primary */
                    } else if (dimension_id == 3) { /* Harmonia */
                        type = 3; /* Integration */
                    } else if (dimension_id == 4) { /* Helix */
                        type = 4; /* Rotation */
                    } else {
                        type = 0; /* Perception if secondary */
                    }
                    
                    assign_node_to_agent(kernel, agent_id, i, type);
                }
            }
        }
    }
    
    /* Create initial connections between core nodes */
    connect_nodes(kernel, 0, 3, 0.7);  /* truth -> wisdom */
    connect_nodes(kernel, 3, 0, 0.7);  /* wisdom -> truth (bidirectional) */
    connect_nodes(kernel, 0, 5, 0.9);  /* truth -> clarity */
    connect_nodes(kernel, 1, 4, 0.8);  /* beauty -> compassion */
    connect_nodes(kernel, 2, 4, 0.8);  /* good -> compassion */
    connect_nodes(kernel, 3, 4, 0.9);  /* wisdom -> compassion */
    connect_nodes(kernel, 4, 2, 0.7);  /* compassion -> good */
    connect_nodes(kernel, 5, 0, 0.8);  /* clarity -> truth */
    connect_nodes(kernel, 6, 7, 0.6);  /* time -> space */
    connect_nodes(kernel, 7, 6, 0.6);  /* space -> time */
    connect_nodes(kernel, 6, 0, 0.5);  /* time -> truth */
    connect_nodes(kernel, 7, 1, 0.6);  /* space -> beauty */
    connect_nodes(kernel, 8, 9, 0.7);  /* rotation -> recursion */
    connect_nodes(kernel, 9, 8, 0.5);  /* recursion -> rotation */
    connect_nodes(kernel, 8, 6, 0.4);  /* rotation -> time */
    connect_nodes(kernel, 9, 0, 0.3);  /* recursion -> truth */
    
    /* Initialize balance between dimensions as equal */
    for (i = 0; i < kernel->dimension_count * kernel->dimension_count; i++) {
        kernel->dimension_balance[i] = 1.0 / kernel->dimension_count;
    }
    
    /* Set initial evolutionary priorities */
    update_evolutionary_priorities(kernel);
}

/* Initialize dimension processors */
void init_dimension_processors(Kernel *kernel) {
    if (!kernel) return;
    
    /* Start with 5 dimensions - 4D spacetime plus Helix for rotation/recursion */
    add_dimension_processor(kernel, "spatial_x_processor", "spatial-x", 0.9, 0.1);  /* High priority, low rotation */
    add_dimension_processor(kernel, "spatial_y_processor", "spatial-y", 0.7, 0.2);  /* Medium priority, some rotation */
    add_dimension_processor(kernel, "temporal_processor", "temporal", 0.8, 0.3);    /* High-medium priority, some rotation */
    add_dimension_processor(kernel, "integration_processor", "integration", 0.4, 0.5); /* Low priority, medium rotation */
    add_dimension_processor(kernel, "helix_processor", "helix", 0.3, 1.0);          /* Lowest priority, maximum rotation */
}

/* Add a new dimension processor */
void add_dimension_processor(Kernel *kernel, const char *name, const char *dimension_type, 
                             double priority, double rotation_factor) {
    DimensionProcessor *processor;
    int dimension_id;
    
    if (!kernel || kernel->dimension_count >= kernel->max_dimensions) return;
    
    dimension_id = kernel->dimension_count;
    processor = &kernel->dimensions[dimension_id];
    
    /* Initialize the new processor */
    strncpy(processor->name, name, MAX_NAME_LENGTH - 1);
    processor->name[MAX_NAME_LENGTH - 1] = '\0';
    
    strncpy(processor->dimension_type, dimension_type, MAX_NAME_LENGTH - 1);
    processor->dimension_type[MAX_NAME_LENGTH - 1] = '\0';
    
    processor->primary_agent = dimension_id; /* Will be set to actual agent later */
    processor->activation = 0.5;
    processor->efficiency = 0.9 - (0.05 * dimension_id); /* Slight efficiency decrease for higher dimensions */
    processor->energy = 1.0;
    processor->focus = 0.8 - (0.05 * dimension_id); /* Slight focus decrease for higher dimensions */
    processor->complexity = 0.2 + (0.1 * dimension_id); /* Higher dimensions have higher complexity */
    processor->priority = priority; /* Evolutionary priority */
    processor->rotation_factor = rotation_factor; /* How much this processor handles rotation */
    processor->stress_response = 1.0 - priority; /* Inverse of priority for stress response */
    processor->entropy = 0.3; /* Initial low entropy */
    processor->health = 0.7; /* Initial good health */
    
    /* Allocate memory for node influence arrays */
    processor->node_influences = (double*)calloc(kernel->max_nodes, sizeof(double));
    processor->node_affinities = (double*)calloc(kernel->max_nodes, sizeof(double));
    
    if (!processor->node_influences || !processor->node_affinities) {
        /* Handle allocation failure */
        if (processor->node_influences) free(processor->node_influences);
        if (processor->node_affinities) free(processor->node_affinities);
        return;
    }
    
    /* Initialize all node affinities to a low baseline */
    {
        int i;
        for (i = 0; i < kernel->max_nodes; i++) {
            processor->node_affinities[i] = 0.1;
        }
    }
    
    /* Update dimension count */
    kernel->dimension_count++;
    
    /* If adding beyond initial dimensions, auto-wire it */
    if (dimension_id >= INITIAL_DIMENSIONS) {
        auto_wire_new_dimension(kernel, dimension_id);
    }
}

/* Auto-wire a newly added dimension */
void auto_wire_new_dimension(Kernel *kernel, int new_dimension_id) {
    int i, j;
    char agent_name[MAX_NAME_LENGTH];
    
    if (!kernel || new_dimension_id < 0 || new_dimension_id >= kernel->dimension_count) return;
    
    /* Create a new agent for this dimension */
    sprintf(agent_name, "agent_dim_%d", new_dimension_id);
    create_agent(kernel, agent_name, 0.03 + ((double)rand() / RAND_MAX) * 0.03, 
                0.7 + ((double)rand() / RAND_MAX) * 0.2, new_dimension_id);
    
    /* Set the primary agent for this dimension */
    kernel->dimensions[new_dimension_id].primary_agent = kernel->agent_count - 1;
    
    /* Establish affinities for each node */
    for (i = 0; i < kernel->node_count; i++) {
        /* Base affinity on node's layer - deeper layers more likely to connect to new dimensions */
        double base_affinity = 0.1 + (0.02 * kernel->nodes[i].layer);
        
        /* Randomize slightly */
        double affinity = base_affinity + ((double)rand() / RAND_MAX) * 0.3;
        
        /* Cap at 0.8 to avoid complete dominance */
        if (affinity > 0.8) affinity = 0.8;
        
        /* Set affinity */
        kernel->dimensions[new_dimension_id].node_affinities[i] = affinity;
    }
    
    /* Create connections between this dimension and others */
    for (i = 0; i < new_dimension_id; i++) {
        int balance_idx1 = i * kernel->max_dimensions + new_dimension_id;
        int balance_idx2 = new_dimension_id * kernel->max_dimensions + i;
        
        /* Set initial balance between dimensions */
        kernel->dimension_balance[balance_idx1] = 0.5;
        kernel->dimension_balance[balance_idx2] = 0.5;
    }
    
    /* Connect nodes to the new agent */
    for (i = 0; i < kernel->node_count; i++) {
        double affinity = kernel->dimensions[new_dimension_id].node_affinities[i];
        
        /* Connect high-affinity nodes to agent */
        if (affinity > 0.6) {
            assign_node_to_agent(kernel, kernel->dimensions[new_dimension_id].primary_agent, i, 1); /* Control */
        } else if (affinity > 0.3) {
            assign_node_to_agent(kernel, kernel->dimensions[new_dimension_id].primary_agent, i, 0); /* Perception */
        }
    }
    
    /* Create new connections between existing nodes based on new dimension */
    for (i = 0; i < kernel->node_count; i++) {
        for (j = 0; j < kernel->node_count; j++) {
            if (i != j && 
                kernel->dimensions[new_dimension_id].node_affinities[i] > 0.4 &&
                kernel->dimensions[new_dimension_id].node_affinities[j] > 0.4 &&
                rand() % 5 == 0) /* 20% chance */
            {
                double weight = 0.3 + ((double)rand() / RAND_MAX) * 0.4; /* 0.3 to 0.7 */
                connect_nodes(kernel, i, j, weight);
            }
        }
    }
    
    printf("[Instance %d] Auto-wired new dimension: %s (ID: %d)\n", 
           instance_id, kernel->dimensions[new_dimension_id].name, new_dimension_id);
}

/* Main function */
int main(int argc, char *argv[]) {
    Kernel *multi_dim_kernel;
    time_t current_time;
    int hour_count = 0;
    int meta_cycle_counter = 0;
    int i;
    
    /* Process command line args (passed when spawning) */
    if (argc > 1) {
        /* Format: instance_id,parent_id,generation,name */
        char *token;
        char *arg_copy = strdup(argv[1]);
        
        if (arg_copy) {
            token = strtok(arg_copy, ",");
            if (token) instance_id = atoi(token);
            
            token = strtok(NULL, ",");
            if (token) parent_id = atoi(token);
            
            token = strtok(NULL, ",");
            if (token) generation = atoi(token);
            
            token = strtok(NULL, ",");
            if (token) strncpy(instance_name, token, MAX_NAME_LENGTH - 1);
            
            free(arg_copy);
            
            /* Child instances run in modular mode */
            is_monolith = 0;
        }
    }
    
    /* Set up signal handlers */
    signal(SIGINT, handle_signal);
    signal(SIGTERM, handle_signal);
    
    /* Detect environment if no args passed */
    if (argc <= 1) {
        detect_environment();
    }
    
    /* Initialize meta-agent */
    init_meta_agent(&kernel_meta);
    
    /* Register this instance */
    register_instance();
    
    /* Initialize instance tracking array */
    for (i = 0; i < MAX_INSTANCES; i++) {
        instances[i].process_id = -1;
        instances[i].generation = 0;
        instances[i].is_alive = 0;
    }
    
    /* Create and initialize kernel */
    multi_dim_kernel = create_kernel(MAX_NODES, MAX_AGENTS, MAX_DIMENSIONS, MAX_LAYERS);
    if (!multi_dim_kernel) {
        printf("[Instance %d] Error: Could not allocate memory for kernel\n", instance_id);
        return 1;
    }
    
    /* Initialize the kernel */
    init_kernel(multi_dim_kernel);
    
    /* Create a complex network */
    printf("[Instance %d] Creating neural network...\n", instance_id);
    create_network(multi_dim_kernel, 6, 24);  /* 6 layers, 24 nodes per layer */
    
    /* Create meta-concept nodes */
    printf("[Instance %d] Creating meta-concept nodes...\n", instance_id);
    create_meta_concepts(multi_dim_kernel);
    
    /* Create recursive nodes */
    printf("[Instance %d] Creating recursive self-reference nodes...\n", instance_id);
    create_recursive_nodes(multi_dim_kernel);
    
    /* Record start time */
    start_time = time(NULL);
    last_save_time = start_time;
    
    /* Initial scan by meta-agent */
    printf("\n[Instance %d] Performing initial system scan...\n", instance_id);
    scan_kernel(multi_dim_kernel, &kernel_meta);
    
    /* Print initial state */
    printf("\n[Instance %d] Starting multi-dimensional kernel with %d processors and meta-agent\n", 
           instance_id, multi_dim_kernel->dimension_count);
    printf("[Instance %d] Initial configuration: %d nodes, %d agents\n", 
           instance_id, multi_dim_kernel->node_count, multi_dim_kernel->agent_count);
    printf("[Instance %d] Initial entropy: %.4f, stability: %.4f\n", 
           instance_id, multi_dim_kernel->entropy, multi_dim_kernel->stability);
    printf("[Instance %d] Initial stress: %.4f, Harmonia priority: %.4f\n",
           instance_id, multi_dim_kernel->stress_level, multi_dim_kernel->harmonia_priority);
    printf("[Instance %d] Generation: %d, Parent ID: %d\n",
           instance_id, generation, parent_id);
    printf("[Instance %d] Dimensions: ", instance_id);
    {
        for (i = 0; i < multi_dim_kernel->dimension_count; i++) {
            printf("%s(%.2f)", 
                   multi_dim_kernel->dimensions[i].dimension_type,
                   multi_dim_kernel->dimensions[i].priority);
            if (i < multi_dim_kernel->dimension_count - 1) printf(", ");
        }
    }
    printf("\n");
    printf("[Instance %d] Press Ctrl+C to gracefully terminate\n\n", instance_id);
    
    /* Run indefinitely */
    while (running) {
        /* Run a batch of iterations without checks for performance */
        for (i = 0; i < REPORT_INTERVAL && running; i++) {
            propagate_values(multi_dim_kernel);
            update_agents(multi_dim_kernel);
            update_dimension_processors(multi_dim_kernel);
            reduce_entropy(multi_dim_kernel);
            step_count++;
            
            /* Meta-agent periodic cycles */
            meta_cycle_counter++;
            if (meta_cycle_counter >= 10000) { /* Meta-agent acts every 10K steps */
                meta_agent_cycle(multi_dim_kernel, &kernel_meta);
                meta_cycle_counter = 0;
            }
            
            /* Periodically adjust stress level to simulate environmental changes */
            if (step_count % 100000 == 0) {
                double new_stress = ((double)rand() / RAND_MAX) * 0.8; /* 0 to 0.8 */
                set_system_stress(multi_dim_kernel, new_stress);
            }
        }
        
        /* Check time and report status after batch */
        current_time = time(NULL);
        
        /* Report status */
        printf("\n[Instance %d] Step %lu: Entropy=%.4f, Stability=%.4f, Coherence=%.4f\n",
               instance_id, step_count, 
               multi_dim_kernel->entropy, 
               multi_dim_kernel->stability, 
               multi_dim_kernel->coherence);
               
        /* Report meta-agent status */
        printf("[Instance %d] Health=%.4f, Meta-awareness=%.4f, Repro=%.4f, Children=%d\n",
               instance_id,
               kernel_meta.system_health,
               kernel_meta.meta_awareness,
               kernel_meta.reproduction_urge,
               kernel_meta.child_count);
        
        /* Report recursive depth */
        printf("[Instance %d] Recursive depth: %.4f, Stress level: %.2f\n", 
               instance_id,
               multi_dim_kernel->recursive_depth,
               multi_dim_kernel->stress_level);
        
        /* Report dimension status */
        printf("[Instance %d] Dimension status: ", instance_id);
        {
            for (i = 0; i < multi_dim_kernel->dimension_count; i++) {
                printf("%s=%.2f(p:%.2f)", 
                       multi_dim_kernel->dimensions[i].dimension_type,
                       multi_dim_kernel->dimensions[i].activation,
                       multi_dim_kernel->dimensions[i].priority);
                if (i < multi_dim_kernel->dimension_count - 1) printf(", ");
            }
        }
        printf("\n");
        
        /* Print performance every hour of runtime */
        if (difftime(current_time, start_time) >= hour_count * 3600) {
            hour_count++;
            print_performance_stats();
        }
        
        /* Save state every 30 minutes */
        if (difftime(current_time, last_save_time) >= 1800) {
            char filename[64];
            snprintf(filename, sizeof(filename), "instance_%d_state_%lu.bin", 
                    instance_id, step_count);
            save_kernel_state(multi_dim_kernel, filename);
            printf("[Instance %d] State saved to %s\n", instance_id, filename);
            last_save_time = current_time;
        }
    }
    
    /* Final save before exit */
    {
        char filename[64];
        snprintf(filename, sizeof(filename), "instance_%d_final_state.bin", instance_id);
        save_kernel_state(multi_dim_kernel, filename);
        printf("[Instance %d] Final state saved to %s\n", instance_id, filename);
    }
    
    /* Print final statistics */
    printf("\n[Instance %d] Final statistics:\n", instance_id);
    printf("[Instance %d] Simulation ran for %lu steps\n", instance_id, step_count);
    printf("[Instance %d] Final entropy: %.4f, stability: %.4f, coherence: %.4f\n", 
           instance_id, multi_dim_kernel->entropy, 
           multi_dim_kernel->stability, 
           multi_dim_kernel->coherence);
    printf("[Instance %d] Final stress: %.4f, Harmonia priority: %.4f\n",
           instance_id, multi_dim_kernel->stress_level, multi_dim_kernel->harmonia_priority);
    printf("[Instance %d] Final recursive depth: %.4f\n",
           instance_id, multi_dim_kernel->recursive_depth);
    printf("[Instance %d] Meta-agent health: %.4f, improvements applied: %d\n",
           instance_id, kernel_meta.system_health, kernel_meta.improvements_applied);
    printf("[Instance %d] Children spawned: %d, Mutations: %d\n",
           instance_id, kernel_meta.child_count, kernel_meta.mutations_applied);
    printf("[Instance %d] Generation: %d\n", instance_id, generation);
    printf("[Instance %d] Dimension count: %d\n", instance_id, multi_dim_kernel->dimension_count);
    
    /* Clean up */
    destroy_kernel(multi_dim_kernel);
    
    return 0;
}

/* Create a complex network */
void create_network(Kernel *kernel, int depth, int breadth) {
    int i, j, layer_start, prev_layer_start;
    double weight;
    
    if (!kernel || depth >= MAX_LAYERS) return;
    
    layer_start = kernel->node_count;
    
    /* Create layers of nodes */
    for (i = 1; i <= depth; i++) { /* Start at layer 1 since layer 0 is for core concepts */
        prev_layer_start = layer_start;
        
        for (j = 0; j < breadth; j++) {
            char name[MAX_NAME_LENGTH];
            
            sprintf(name, "node_l%d_n%d", i, j);
            create_node(kernel, name, (double)rand() / RAND_MAX, 
                      0.2 + 0.3 * ((double)rand() / RAND_MAX), i);
            
            /* Set dimension affinities based on position in network */
            {
                int d;
                for (d = 0; d < kernel->dimension_count && d < 5; d++) {
                    double affinity = 0.1;
                    
                    /* Distribute affinity based on position */
                    if (d == 0 && j % 5 == 0) affinity = 0.7; /* Spatial-X */
                    if (d == 1 && j % 5 == 1) affinity = 0.7; /* Spatial-Y */
                    if (d == 2 && j % 5 == 2) affinity = 0.7; /* Temporal */
                    if (d == 3 && j % 5 == 3) affinity = 0.7; /* Integration */
                    if (d == 4 && j % 5 == 4) affinity = 0.7; /* Helix */
                    
                    /* Add some randomness */
                    affinity += ((double)rand() / RAND_MAX) * 0.2 - 0.1;
                    
                    /* Keep in valid range */
                    if (affinity < 0.1) affinity = 0.1;
                    if (affinity > 0.9) affinity = 0.9;
                    
                    set_node_dimension_affinity(kernel, kernel->node_count - 1, d, affinity);
                }
            }
            
            /* Set rotation values with increasing probability in deeper layers */
            if (rand() % 10 < i) { /* More likely in deeper layers */
                kernel->nodes[kernel->node_count - 1].rotation = 
                    ((double)rand() / RAND_MAX) * 0.5; /* 0 to 0.5 */
                kernel->nodes[kernel->node_count - 1].angular_momentum = 
                    ((double)rand() / RAND_MAX) * 0.4; /* 0 to 0.4 */
                
                /* Random spin direction */
                if (rand() % 2 == 0) {
                    kernel->nodes[kernel->node_count - 1].spin_direction = 1.0;
                } else {
                    kernel->nodes[kernel->node_count - 1].spin_direction = -1.0;
                }
            }
        }
        
        /* Connect to previous layer */
        if (i > 1) {
            int k, l;
            for (k = prev_layer_start; k < prev_layer_start + breadth && k < kernel->node_count; k++) {
                for (l = layer_start; l < layer_start + breadth && l < kernel->node_count; l++) {
                    /* Create sparse connections */
                    if (rand() % 4 == 0) { /* 1/4 chance of connection */
                        weight = ((double)rand() / RAND_MAX) * 2.0 - 1.0; /* -1.0 to 1.0 */
                        connect_nodes(kernel, k, l, weight);
                    }
                }
            }
        }
        
        /* Connect to core concepts from layer 0 */
        for (j = layer_start; j < layer_start + breadth && j < kernel->node_count; j++) {
            int core_node = rand() % kernel->layer_counts[0];
            weight = 0.3 + ((double)rand() / RAND_MAX) * 0.5; /* 0.3 to 0.8 */
weight = 0.3 + ((double)rand() / RAND_MAX) * 0.5; /* 0.3 to 0.8 */
           connect_nodes(kernel, core_node, j, weight);
       }
       
       layer_start += breadth;
   }
}

/* Create meta-concepts for higher-order thinking */
void create_meta_concepts(Kernel *kernel) {
   int i, j;
   int meta_layer = MAX_LAYERS - 1;
   
   /* Create meta-concept nodes */
   create_node(kernel, "uncertainty", 0.2, 0.4, meta_layer);
   create_node(kernel, "paradox", 0.3, 0.5, meta_layer);
   create_node(kernel, "creativity", 0.6, 0.3, meta_layer);
   create_node(kernel, "integrity", 0.7, 0.4, meta_layer);
   create_node(kernel, "emergence", 0.5, 0.6, meta_layer);
   create_node(kernel, "harmony", 0.8, 0.3, meta_layer);
   create_node(kernel, "duality", 0.5, 0.5, meta_layer);
   create_node(kernel, "self_reference", 0.4, 0.7, meta_layer);
   create_node(kernel, "transcendence", 0.3, 0.8, meta_layer);
   create_node(kernel, "unity", 0.7, 0.6, meta_layer);
   
   /* Set dimension affinities for meta-concepts */
   for (i = 0; i < 10; i++) {
       int node_id = kernel->node_count - 10 + i;
       
       /* Different meta-concepts have different dimensional affinities */
       switch (i) {
           case 0: /* uncertainty */
               set_node_dimension_affinity(kernel, node_id, 2, 0.8); /* Strong temporal */
               set_node_dimension_affinity(kernel, node_id, 4, 0.6); /* Medium helix */
               break;
           case 1: /* paradox */
               set_node_dimension_affinity(kernel, node_id, 0, 0.5); /* Equal spatial-x */
               set_node_dimension_affinity(kernel, node_id, 1, 0.5); /* Equal spatial-y */
               set_node_dimension_affinity(kernel, node_id, 4, 0.8); /* Strong helix */
               break;
           case 2: /* creativity */
               set_node_dimension_affinity(kernel, node_id, 1, 0.7); /* Strong spatial-y */
               set_node_dimension_affinity(kernel, node_id, 4, 0.7); /* Strong helix */
               break;
           case 3: /* integrity */
               set_node_dimension_affinity(kernel, node_id, 0, 0.8); /* Strong spatial-x */
               set_node_dimension_affinity(kernel, node_id, 3, 0.6); /* Medium integration */
               break;
           case 4: /* emergence */
               set_node_dimension_affinity(kernel, node_id, 3, 0.9); /* Very strong integration */
               set_node_dimension_affinity(kernel, node_id, 4, 0.6); /* Medium helix */
               break;
           case 5: /* harmony */
               set_node_dimension_affinity(kernel, node_id, 3, 0.8); /* Strong integration */
               set_node_dimension_affinity(kernel, node_id, 1, 0.6); /* Medium spatial-y */
               break;
           case 6: /* duality */
               for (j = 0; j < kernel->dimension_count; j++) {
                   set_node_dimension_affinity(kernel, node_id, j, 0.5); /* Equal across all */
               }
               set_node_dimension_affinity(kernel, node_id, 4, 0.7); /* Stronger helix */
               break;
           case 7: /* self_reference */
               set_node_dimension_affinity(kernel, node_id, 0, 0.6); /* Moderate spatial-x */
               set_node_dimension_affinity(kernel, node_id, 2, 0.6); /* Moderate temporal */
               set_node_dimension_affinity(kernel, node_id, 4, 0.9); /* Very strong helix */
               break;
           case 8: /* transcendence */
               for (j = 0; j < kernel->dimension_count; j++) {
                   set_node_dimension_affinity(kernel, node_id, j, 0.7); /* High across all */
               }
               break;
           case 9: /* unity */
               set_node_dimension_affinity(kernel, node_id, 3, 0.9); /* Very strong integration */
               break;
       }
       
       /* Set rotation properties for recursion-related concepts */
       if (i == 1 || i == 6 || i == 7) { /* paradox, duality, self-reference */
           kernel->nodes[node_id].rotation = 0.4 + ((double)rand() / RAND_MAX) * 0.3; /* 0.4 to 0.7 */
           kernel->nodes[node_id].angular_momentum = 0.3 + ((double)rand() / RAND_MAX) * 0.3; /* 0.3 to 0.6 */
       }
   }
   
   /* Connect meta-concepts to nodes in earlier layers */
   for (i = kernel->node_count - 10; i < kernel->node_count; i++) {
       /* Connect each meta concept to multiple nodes */
       for (j = 0; j < kernel->node_count - 10; j++) {
           if (rand() % 20 == 0) { /* 5% chance of connection */
               double weight = 0.4 + ((double)rand() / RAND_MAX) * 0.5; /* 0.4 to 0.9 */
               connect_nodes(kernel, j, i, weight);  /* Node to meta concept */
               
               if (rand() % 3 == 0) { /* 33% chance of bidirectional */
                   connect_nodes(kernel, i, j, weight * 0.7);  /* Meta concept back to node (weaker) */
               }
           }
       }
   }
   
   /* Interconnect meta-concepts for horizontal integration */
   for (i = kernel->node_count - 10; i < kernel->node_count; i++) {
       for (j = kernel->node_count - 10; j < kernel->node_count; j++) {
           if (i != j && rand() % 3 == 0) {  /* 1/3 chance of connection */
               double weight = 0.3 + ((double)rand() / RAND_MAX) * 0.4; /* 0.3 to 0.7 */
               connect_nodes(kernel, i, j, weight);
           }
       }
   }
   
   /* Add meta-concepts to agents as concept nodes (type 2), rotation nodes (type 4), or integration nodes (type 3) */
   for (i = kernel->node_count - 10; i < kernel->node_count; i++) {
       int node_id = i;
       
       /* Find which dimension has highest affinity */
       int highest_dim = 0;
       double highest_affinity = 0;
       
       for (j = 0; j < kernel->dimension_count; j++) {
           double affinity = kernel->dimensions[j].node_affinities[node_id];
           if (affinity > highest_affinity) {
               highest_affinity = affinity;
               highest_dim = j;
           }
       }
       
       /* Assign to primary agent of that dimension with appropriate type */
       if (highest_dim < kernel->dimension_count) {
           int agent_id = kernel->dimensions[highest_dim].primary_agent;
           if (agent_id >= 0 && agent_id < kernel->agent_count) {
               int node_type;
               
               /* Determine node type based on dimension */
               if (highest_dim == 3) { /* Harmonia */
                   node_type = 3; /* Integration node */
               } else if (highest_dim == 4) { /* Helix */
                   node_type = 4; /* Rotation node */
               } else {
                   node_type = 2; /* Concept node */
               }
               
               assign_node_to_agent(kernel, agent_id, node_id, node_type);
           }
       }
   }
}

/* Create specifically recursive nodes for self-reference */
void create_recursive_nodes(Kernel *kernel) {
   int i, start_node, core_nodes[5];
   int meta_layer = MAX_LAYERS - 2; /* Just before meta-concepts */
   
   if (kernel->node_count < 10) return; /* Need core nodes */
   
   /* Store references to key nodes */
   for (i = 0; i < 5 && i < kernel->dimension_count; i++) {
       /* Get a primary node from each dimension's agent */
       int agent_id = kernel->dimensions[i].primary_agent;
       if (agent_id >= 0 && agent_id < kernel->agent_count) {
           Agent *agent = &kernel->agents[agent_id];
           if (agent->control_count > 0) {
               core_nodes[i] = agent->control_nodes[0];
           } else {
               core_nodes[i] = i; /* Fallback to dimension index */
           }
       } else {
           core_nodes[i] = i; /* Default */
       }
   }
   
   /* Create special recursive nodes */
   start_node = kernel->node_count;
   
   create_node(kernel, "self_model", 0.1, 0.7, meta_layer);
   create_node(kernel, "recursive_loop", 0.2, 0.6, meta_layer);
   create_node(kernel, "meta_awareness", 0.3, 0.5, meta_layer);
   create_node(kernel, "self_reference", 0.2, 0.8, meta_layer);
   create_node(kernel, "observer", 0.4, 0.6, meta_layer);
   
   /* Set strong helix affinity for all recursive nodes */
   for (i = 0; i < 5; i++) {
       int node_id = start_node + i;
       set_node_dimension_affinity(kernel, node_id, 4, 0.9); /* Very strong helix */
       
       /* Secondary affinities */
       if (i == 0) { /* self_model */
           set_node_dimension_affinity(kernel, node_id, 0, 0.6); /* Medium aletheia */
       } else if (i == 1) { /* recursive_loop */
           set_node_dimension_affinity(kernel, node_id, 2, 0.7); /* Strong chronos */
       } else if (i == 2) { /* meta_awareness */
           set_node_dimension_affinity(kernel, node_id, 3, 0.7); /* Strong harmonia */
       } else if (i == 3) { /* self_reference */
           set_node_dimension_affinity(kernel, node_id, 2, 0.5); /* Medium chronos */
           set_node_dimension_affinity(kernel, node_id, 3, 0.5); /* Medium harmonia */
       } else if (i == 4) { /* observer */
           set_node_dimension_affinity(kernel, node_id, 1, 0.6); /* Medium sophia */
       }
       
       /* Set rotation properties */
       kernel->nodes[node_id].rotation = 0.5;
       kernel->nodes[node_id].angular_momentum = 0.5;
       kernel->nodes[node_id].spin_direction = (i % 2 == 0) ? 1.0 : -1.0; /* Alternating */
   }
   
   /* Create recursive connections */
   /* Each node connects to itself */
   for (i = 0; i < 5; i++) {
       int node_id = start_node + i;
       connect_nodes(kernel, node_id, node_id, 0.3); /* Self-connection with moderate weight */
   }
   
   /* Circular connections */
   for (i = 0; i < 5; i++) {
       int node_id = start_node + i;
       int next_id = start_node + ((i + 1) % 5);
       connect_nodes(kernel, node_id, next_id, 0.7); /* Strong forward connection */
       connect_nodes(kernel, next_id, node_id, 0.4); /* Weaker backward connection */
   }
   
   /* Connect to dimension representatives */
   for (i = 0; i < 5; i++) {
       int recur_id = start_node + i;
       int dim_id = i < 5 ? core_nodes[i] : 0;
       
       if (dim_id >= 0 && dim_id < kernel->node_count) {
           /* Create bidirectional connections */
           connect_nodes(kernel, recur_id, dim_id, 0.6);
           connect_nodes(kernel, dim_id, recur_id, 0.5);
       }
   }
   
   /* Assign recursive nodes to Helix agent */
   if (kernel->dimension_count > 4) {
       int helix_agent = kernel->dimensions[4].primary_agent;
       if (helix_agent >= 0 && helix_agent < kernel->agent_count) {
           for (i = 0; i < 5; i++) {
               assign_node_to_agent(kernel, helix_agent, start_node + i, 4); /* Rotation nodes */
           }
       }
   }
}

/* Print performance statistics */
void print_performance_stats(void) {
   time_t current_time = time(NULL);
   double elapsed = difftime(current_time, start_time);
   double steps_per_second = step_count / (elapsed > 0 ? elapsed : 1);
   
   printf("[Instance %d] Running for %.2f seconds\n", instance_id, elapsed);
   printf("[Instance %d] Completed %lu steps\n", instance_id, step_count);
   printf("[Instance %d] Performance: %.2f steps/second\n", instance_id, steps_per_second);
}

/* Update evolutionary priorities based on stress */
void update_evolutionary_priorities(Kernel *kernel) {
   int i;
   double stress = kernel->stress_level;
   
   if (!kernel) return;
   
   /* Adjust processor priorities based on stress level */
   for (i = 0; i < kernel->dimension_count; i++) {
       DimensionProcessor *processor = &kernel->dimensions[i];
       double base_priority = processor->priority;
       double stress_response = processor->stress_response;
       
       /* Under stress, high-priority processors get even higher priority */
       if (base_priority > 0.7) { /* High priority processors (Aletheia, Chronos) */
           processor->priority = base_priority + (stress * 0.3); /* Boost under stress */
       } 
       /* Medium priority becomes variable */
       else if (base_priority > 0.5) { /* Medium processors (Sophia) */
           processor->priority = base_priority + (stress * 0.1) - (stress * stress * 0.2);
       }
       /* Low priority processors get suppressed under stress */
       else { /* Low priority processors (Harmonia, Helix) */
           processor->priority = base_priority * (1.0 - stress * 0.7);
       }
       
       /* Ensure bounds */
       if (processor->priority > 1.0) processor->priority = 1.0;
       if (processor->priority < 0.1) processor->priority = 0.1;
       
       /* Update agent priorities */
       if (processor->primary_agent >= 0 && processor->primary_agent < kernel->agent_count) {
           kernel->agents[processor->primary_agent].evolutionary_priority = processor->priority;
       }
   }
   
   /* Update Harmonia's specific priority separately */
   kernel->harmonia_priority = kernel->dimensions[3].priority;
}

/* Set system stress level */
void set_system_stress(Kernel *kernel, double stress_level) {
   if (!kernel) return;
   
   /* Clamp stress to valid range */
   if (stress_level < 0.0) stress_level = 0.0;
   if (stress_level > 1.0) stress_level = 1.0;
   
   kernel->stress_level = stress_level;
   
   /* Update priorities based on new stress level */
   update_evolutionary_priorities(kernel);
   
   printf("[Instance %d] System stress level set to %.2f\n", instance_id, stress_level);
   printf("[Instance %d] Updated processor priorities:\n", instance_id);
   
   {
       int i;
       for (i = 0; i < kernel->dimension_count; i++) {
           printf("  %s: %.2f\n", 
                  kernel->dimensions[i].dimension_type,
                  kernel->dimensions[i].priority);
       }
   }
}

/* Main propagation function */
void propagate_values(Kernel *kernel) {
   int i;
   
   if (!kernel) return;
   
   /* Execute each dimension's propagation cycle with priority weighting */
   for (i = 0; i < kernel->dimension_count; i++) {
       execute_dimension_cycle(kernel, i);
   }
   
   /* Process interaction between dimensions */
   dimension_interaction(kernel);
   
   /* Process rotation dynamics */
   process_rotation_dynamics(kernel);
   
   /* Update global time */
   kernel->global_time += 1.0;
   
   /* Increase entropy */
   kernel->entropy += 0.01;
   if (kernel->entropy > 1.0) kernel->entropy = 1.0;
}

/* Process rotation dynamics for Helix dimension */
void process_rotation_dynamics(Kernel *kernel) {
   int i, j;
   double helix_influence = 0.0;
   
   if (!kernel) return;
   
   /* Find Helix dimension influence */
   for (i = 0; i < kernel->dimension_count; i++) {
       if (strcmp(kernel->dimensions[i].dimension_type, "helix") == 0) {
           helix_influence = kernel->dimensions[i].activation * kernel->dimensions[i].priority;
           break;
       }
   }
   
   /* Update rotation values for nodes */
   for (i = 0; i < kernel->node_count; i++) {
       Node *node = &kernel->nodes[i];
       double rotation_factor = 0.0;
       
       /* Calculate rotation influence from connected nodes */
       for (j = 0; j < node->connection_count; j++) {
           int target = node->connections[j];
           if (target >= 0 && target < kernel->node_count) {
               rotation_factor += kernel->nodes[target].rotation * node->weights[j] * 0.2;
           }
       }
       
       /* Apply helix influence */
       rotation_factor += helix_influence * 0.1;
       
       /* Update rotation */
       node->rotation += node->angular_momentum * node->spin_direction * rotation_factor;
       
       /* Apply constraints */
       if (node->rotation > 1.0) {
           node->rotation = 1.0;
           /* Possible direction change on hitting max */
           if (rand() % 4 == 0) { /* 25% chance */
               node->spin_direction *= -1.0;
           }
       }
       if (node->rotation < -1.0) {
           node->rotation = -1.0;
           /* Possible direction change on hitting min */
           if (rand() % 4 == 0) { /* 25% chance */
               node->spin_direction *= -1.0;
           }
       }
       
       /* Angular momentum decays slightly */
       node->angular_momentum *= 0.99;
       
       /* Minimum momentum */
       if (node->angular_momentum < 0.01) {
           node->angular_momentum = 0.01;
       }
   }
   
   /* Update recursive depth based on key node rotations */
   if (kernel->node_count > 9) { /* If we have recursion node */
       kernel->recursive_depth = kernel->nodes[9].rotation * 0.7 + kernel->nodes[9].value * 0.3;
   }
}

/* Execute a single dimension processor's cycle */
void execute_dimension_cycle(Kernel *kernel, int dimension_id) {
   int i, j;
   double *new_values;
   DimensionProcessor *processor;
   double priority_factor;
   
   if (!kernel || dimension_id < 0 || dimension_id >= kernel->dimension_count) return;
   
   processor = &kernel->dimensions[dimension_id];
   new_values = (double*)malloc(kernel->node_count * sizeof(double));
   
   if (!new_values) return;
   
   /* Apply evolutionary priority to this processor's execution */
   priority_factor = processor->priority;
   
   /* Reset influence values */
   for (i = 0; i < kernel->node_count; i++) {
       processor->node_influences[i] = 0.0;
       new_values[i] = kernel->nodes[i].value; /* Initialize with current values */
   }
   
   /* Calculate new values based on connections */
   for (i = 0; i < kernel->node_count; i++) {
       Node *node = &kernel->nodes[i];
       double input_sum = 0.0;
       double processor_weight;
       
       /* Calculate processor's influence weight on this node */
       processor_weight = processor->node_affinities[i] * processor->activation * priority_factor;
       
       /* Skip nodes that this processor has minimal influence over */
       if (processor_weight < 0.2) {
           continue;
       }
       
       /* Sum inputs from connections */
       for (j = 0; j < node->connection_count; j++) {
           int target = node->connections[j];
           double weight = node->weights[j];
           double target_value = kernel->nodes[target].value;
           
           /* For Helix processor, incorporate rotation */
           if (strcmp(processor->dimension_type, "helix") == 0) {
               /* Modulate connection by rotation state */
               weight *= (1.0 + kernel->nodes[target].rotation * 0.3);
               
               /* Use angular momentum as amplifier */
               target_value *= (1.0 + kernel->nodes[target].angular_momentum * 0.2);
           }
           
           input_sum += target_value * weight;
       }
       
       /* Add memory component */
       input_sum += node->memory * 0.2;
       
       /* Apply processor's focus to the calculation */
       input_sum *= (0.5 + processor->focus * 0.5);
       
       /* Calculate activation using fast sigmoid approximation */
       node->activation = fast_sigmoid(input_sum);
       
       /* Only activate if above threshold */
       if (node->activation > node->threshold) {
           /* Calculate processor's influence on this node */
           processor->node_influences[i] = (node->activation - node->value) * processor_weight;
           
           /* Store new value temporarily */
           new_values[i] = node->value + processor->node_influences[i];
           
           /* For Helix processor, update rotation values */
           if (strcmp(processor->dimension_type, "helix") == 0) {
               /* Stimulate rotation based on activation change */
               node->angular_momentum += fabs(node->activation - node->value) * 0.1;
               if (node->angular_momentum > 1.0) node->angular_momentum = 1.0;
           }
           
           /* Update coherence and entropy */
           node->coherence = (node->coherence * 0.9) + 
                             (1.0 - fabs(node->activation - node->value)) * 0.1;
           
           node->entropy = (node->entropy * 0.95) + 
                          (fabs(node->activation - node->value) * 0.05);
       } else {
           /* Slight decay if not activated */
           new_values[i] = node->value * (0.9 + 0.1 * processor_weight);
           processor->node_influences[i] = (new_values[i] - node->value) * processor_weight;
           
           /* Small entropy increase for inactivity */
           node->entropy += 0.001;
           node->coherence -= 0.001;
       }
       
       /* Ensure bounds */
       if (node->entropy > 1.0) node->entropy = 1.0;
       if (node->entropy < 0.0) node->entropy = 0.0;
       if (node->coherence > 1.0) node->coherence = 1.0;
       if (node->coherence < 0.0) node->coherence = 0.0;
       
       /* Update memory */
       node->memory = node->memory * 0.8 + node->value * 0.2;
   }
   
   /* Apply efficiency factor to all changes */
   for (i = 0; i < kernel->node_count; i++) {
       processor->node_influences[i] *= processor->efficiency;
   }
   
   /* Update processor entropy */
   {
       double sum_entropy = 0.0;
       int count = 0;
       
       /* Calculate average change magnitude as a measure of entropy */
       for (i = 0; i < kernel->node_count; i++) {
           if (processor->node_influences[i] != 0.0) {
               sum_entropy += fabs(processor->node_influences[i]);
               count++;
           }
       }
       
       if (count > 0) {
           double avg_change = sum_entropy / count;
           processor->entropy = processor->entropy * 0.95 + avg_change * 0.5;
           
           /* Ensure bounds */
           if (processor->entropy > 1.0) processor->entropy = 1.0;
       }
   }
   
   free(new_values);
}

/* Process interaction between dimensions and finalize node values */
void dimension_interaction(Kernel *kernel) {
   int i, j, k;
   double *combined_influences;
   
   if (!kernel) return;
   
   combined_influences = (double*)calloc(kernel->node_count, sizeof(double));
   if (!combined_influences) return;
   
   /* Calculate combined influences from all dimensions */
   for (i = 0; i < kernel->node_count; i++) {
       double total_influence = 0.0;
       double total_weight = 0.0;
       
       for (j = 0; j < kernel->dimension_count; j++) {
           DimensionProcessor *processor = &kernel->dimensions[j];
           double influence = processor->node_influences[i];
           double weight = processor->node_affinities[i] * processor->activation * processor->priority;
           
           /* Scale influence by balance factors with other dimensions */
           for (k = 0; k < kernel->dimension_count; k++) {
               if (j != k) {
                   int balance_idx = j * kernel->max_dimensions + k;
                   weight *= kernel->dimension_balance[balance_idx];
               }
           }
           
           total_influence += influence * weight;
           total_weight += weight;
       }
       
       if (total_weight > 0) {
           combined_influences[i] = total_influence / total_weight;
       }
   }
   
   /* Apply combined influences to update node values */
   for (i = 0; i < kernel->node_count; i++) {
       Node *node = &kernel->nodes[i];
       
       /* Apply the change */
       node->value += combined_influences[i];
       
       /* Keep value within bounds */
       if (node->value > 1.0) node->value = 1.0;
       if (node->value < 0.0) node->value = 0.0;
   }
   
   free(combined_influences);
}

/* Reduce entropy based on coherence */
void reduce_entropy(Kernel *kernel) {
   double reduction_rate;
   double dimension_balance_factor = 0.0;
   int i, j, count = 0;
   
   if (!kernel) return;
   
   /* Calculate dimension balance factor */
   for (i = 0; i < kernel->dimension_count; i++) {
       for (j = i+1; j < kernel->dimension_count; j++) {
           int balance_idx1 = i * kernel->max_dimensions + j;
           int balance_idx2 = j * kernel->max_dimensions + i;
           
           double balance1 = kernel->dimension_balance[balance_idx1];
           double balance2 = kernel->dimension_balance[balance_idx2];
           
           /* Reward balanced relationships between dimensions */
           dimension_balance_factor += 1.0 - fabs(balance1 - balance2);
           count++;
       }
   }
   
   if (count > 0) {
       dimension_balance_factor /= count;
   } else {
       dimension_balance_factor = 1.0;
   }
   
   /* Calculate entropy reduction based on harmonia priority */
   reduction_rate = 0.01 * kernel->coherence * dimension_balance_factor * kernel->harmonia_priority;
   
   /* Reduce entropy */
   kernel->entropy -= reduction_rate;
   if (kernel->entropy < 0.0) kernel->entropy = 0.0;
   
   /* Update system stability */
   kernel->stability = 1.0 - kernel->entropy;
   
   /* Recursively update stability through Helix (feedback loop) */
   if (kernel->recursive_depth > 0.3) { /* Only if recursive capability is developed */
       double recursive_boost = kernel->recursive_depth * 0.01;
       kernel->stability += recursive_boost;
       if (kernel->stability > 1.0) kernel->stability = 1.0;
   }
}

/* Connect a node to an agent */
void connect_node(Kernel *kernel, int node_id, int agent_id, int type) {
   if (!kernel || node_id < 0 || node_id >= kernel->node_count || 
       agent_id < 0 || agent_id >= kernel->agent_count) return;
   
   assign_node_to_agent(kernel, agent_id, node_id, type);
}

/* Create a node */
void create_node(Kernel *kernel, const char *name, double initial_value, double threshold, int layer) {
   Node *node;
   int i;
   
   if (!kernel || kernel->node_count >= kernel->max_nodes) return;
   
   node = &kernel->nodes[kernel->node_count];
   strncpy(node->name, name, MAX_NAME_LENGTH - 1);
   node->name[MAX_NAME_LENGTH - 1] = '\0';
   node->value = initial_value;
   node->threshold = threshold;
   node->connection_count = 0;
   node->activation = 0.0;
   node->memory = 0.0;
   node->importance = 0.5;
   node->layer = layer;
   node->rotation = 0.0;
   node->angular_momentum = 0.0;
   node->spin_direction = 1.0; /* Default clockwise */
   node->entropy = 0.3; /* Start with low entropy */
   node->coherence = 0.7; /* Start with decent coherence */
   
   /* Initialize dimension affinities to neutral */
   for (i = 0; i < kernel->max_dimensions; i++) {
       node->dimension_affinity[i] = 0;
   }
   
   /* Update layer count */
   kernel->layer_counts[layer]++;
   
   /* Set initial processor affinities */
   for (i = 0; i < kernel->dimension_count; i++) {
       kernel->dimensions[i].node_affinities[kernel->node_count] = 0.1 + ((double)rand() / RAND_MAX) * 0.1;
   }
   
   kernel->node_count++;
}

/* Save kernel state */
void save_kernel_state(Kernel *kernel, const char *filename) {
   FILE *file;
   int i;
   
   if (!kernel || !filename) return;
   
   file = fopen(filename, "wb");
   if (!file) return;
   
   /* Write kernel configuration values */
   fwrite(&kernel->node_count, sizeof(int), 1, file);
   fwrite(&kernel->agent_count, sizeof(int), 1, file);
   fwrite(&kernel->dimension_count, sizeof(int), 1, file);
   fwrite(&kernel->max_nodes, sizeof(int), 1, file);
   fwrite(&kernel->max_agents, sizeof(int), 1, file);
   fwrite(&kernel->max_dimensions, sizeof(int), 1, file);
   fwrite(&kernel->global_time, sizeof(double), 1, file);
   fwrite(&kernel->stability, sizeof(double), 1, file);
   fwrite(&kernel->entropy, sizeof(double), 1, file);
   fwrite(&kernel->complexity, sizeof(double), 1, file);
   fwrite(&kernel->coherence, sizeof(double), 1, file);
   fwrite(&kernel->stress_level, sizeof(double), 1, file);
   fwrite(&kernel->harmonia_priority, sizeof(double), 1, file);
   fwrite(&kernel->recursive_depth, sizeof(double), 1, file);
   
   /* Write meta-agent data */
   fwrite(&kernel_meta, sizeof(MetaAgent), 1, file);
   
   /* Write nodes */
   for (i = 0; i < kernel->node_count; i++) {
       Node *node = &kernel->nodes[i];
       fwrite(node->name, sizeof(char), MAX_NAME_LENGTH, file);
       fwrite(&node->value, sizeof(double), 1, file);
       fwrite(&node->threshold, sizeof(double), 1, file);
       fwrite(&node->connection_count, sizeof(int), 1, file);
       fwrite(node->connections, sizeof(int), node->connection_count, file);
       fwrite(node->weights, sizeof(double), node->connection_count, file);
       fwrite(&node->activation, sizeof(double), 1, file);
       fwrite(&node->memory, sizeof(double), 1, file);
       fwrite(&node->importance, sizeof(double), 1, file);
       fwrite(&node->layer, sizeof(int), 1, file);
       fwrite(node->dimension_affinity, sizeof(int), kernel->dimension_count, file);
       fwrite(&node->rotation, sizeof(double), 1, file);
       fwrite(&node->angular_momentum, sizeof(double), 1, file);
       fwrite(&node->spin_direction, sizeof(double), 1, file);
       fwrite(&node->entropy, sizeof(double), 1, file);
       fwrite(&node->coherence, sizeof(double), 1, file);
   }
   
   /* Write agents */
   for (i = 0; i < kernel->agent_count; i++) {
       Agent *agent = &kernel->agents[i];
       fwrite(agent->name, sizeof(char), MAX_NAME_LENGTH, file);
       fwrite(&agent->control_count, sizeof(int), 1, file);
       fwrite(agent->control_nodes, sizeof(int), agent->control_count, file);
       fwrite(&agent->perception_count, sizeof(int), 1, file);
       fwrite(agent->perception_nodes, sizeof(int), agent->perception_count, file);
       fwrite(&agent->concept_count, sizeof(int), 1, file);
       fwrite(agent->concept_nodes, sizeof(int), agent->concept_count, file);
       fwrite(&agent->integration_count, sizeof(int), 1, file);
       fwrite(agent->integration_nodes, sizeof(int), agent->integration_count, file);
       fwrite(&agent->rotation_count, sizeof(int), 1, file);
       fwrite(agent->rotation_nodes, sizeof(int), agent->rotation_count, file);
       fwrite(&agent->confidence, sizeof(double), 1, file);
       fwrite(&agent->learning_rate, sizeof(double), 1, file);
       fwrite(&agent->empathy, sizeof(double), 1, file);
       fwrite(&agent->coherence, sizeof(double), 1, file);
       fwrite(&agent->focus, sizeof(double), 1, file);
       fwrite(&agent->integrity, sizeof(double), 1, file);
       fwrite(&agent->evolutionary_priority, sizeof(double), 1, file);
       fwrite(&agent->primary_dimension, sizeof(int), 1, file);
   }
   
   /* Write dimension processors */
   for (i = 0; i < kernel->dimension_count; i++) {
       DimensionProcessor *processor = &kernel->dimensions[i];
       fwrite(processor->name, sizeof(char), MAX_NAME_LENGTH, file);
       fwrite(processor->dimension_type, sizeof(char), MAX_NAME_LENGTH, file);
       fwrite(&processor->primary_agent, sizeof(int), 1, file);
       fwrite(&processor->activation, sizeof(double), 1, file);
       fwrite(&processor->efficiency, sizeof(double), 1, file);
       fwrite(&processor->energy, sizeof(double), 1, file);
       fwrite(&processor->focus, sizeof(double), 1, file);
       fwrite(&processor->complexity, sizeof(double), 1, file);
       fwrite(&processor->priority, sizeof(double), 1, file);
       fwrite(&processor->rotation_factor, sizeof(double), 1, file);
       fwrite(&processor->stress_response, sizeof(double), 1, file);
       fwrite(&processor->entropy, sizeof(double), 1, file);
       fwrite(&processor->health, sizeof(double), 1, file);
       fwrite(processor->node_influences, sizeof(double), kernel->node_count, file);
       fwrite(processor->node_affinities, sizeof(double), kernel->node_count, file);
   }
   
   /* Write dimension balance array */
   fwrite(kernel->dimension_balance, sizeof(double), 
          kernel->dimension_count * kernel->dimension_count, file);
   
   /* Write layer counts */
   fwrite(kernel->layer_counts, sizeof(int), MAX_LAYERS, file);
   
   /* Write instance tracking data */
   fwrite(&instance_count, sizeof(int), 1, file);
   fwrite(instances, sizeof(KernelInstance), instance_count, file);
   
   fclose(file);
   
   printf("[Instance %d] Kernel state saved to %s\n", instance_id, filename);
}

/* Proposal implementations */
void add_stability_node(Kernel *kernel, MetaAgent *meta) {
   int i;
   char name[MAX_NAME_LENGTH];
   int layer = 3; /* Mid-level layer */
   
   if (!kernel || !meta) return;
   
   /* Create a name for the stability node */
   sprintf(name, "stability_node_%lu", step_count);
   
   /* Create the node with high stability properties */
   create_node(kernel, name, 0.7, 0.3, layer);
   
   /* Connect to key nodes for each dimension */
   for (i = 0; i < kernel->dimension_count; i++) {
       int agent_id = kernel->dimensions[i].primary_agent;
       if (agent_id >= 0 && agent_id < kernel->agent_count) {
           Agent *agent = &kernel->agents[agent_id];
           if (agent->control_count > 0) {
               int target_node = agent->control_nodes[0];
               connect_nodes(kernel, kernel->node_count - 1, target_node, 0.6);
               connect_nodes(kernel, target_node, kernel->node_count - 1, 0.4);
           }
       }
   }
   
   /* Set balanced dimension affinities */
   for (i = 0; i < kernel->dimension_count; i++) {
       set_node_dimension_affinity(kernel, kernel->node_count - 1, i, 0.6);
   }
   
   /* Set low rotation and entropy for stability */
   kernel->nodes[kernel->node_count - 1].rotation = 0.1;
   kernel->nodes[kernel->node_count - 1].angular_momentum = 0.1;
   kernel->nodes[kernel->node_count - 1].entropy = 0.1;
   kernel->nodes[kernel->node_count - 1].coherence = 0.9;
   
   printf("[Instance %d] Added stability node: %s\n", instance_id, name);
}

void optimize_dimension(Kernel *kernel, MetaAgent *meta) {
   int dimension_id, i;
   DimensionProcessor *processor;
   
   if (!kernel || !meta) return;
   
   /* Extract target dimension from proposal */
   dimension_id = proposal_queue[0].target_dimension;
   
   if (dimension_id < 0 || dimension_id >= kernel->dimension_count) return;
   
   processor = &kernel->dimensions[dimension_id];
   
   /* 1. Boost energy and efficiency */
   processor->energy = 0.8 + ((double)rand() / RAND_MAX) * 0.2; /* 0.8-1.0 */
   processor->efficiency = 0.8 + ((double)rand() / RAND_MAX) * 0.2; /* 0.8-1.0 */
   
   /* 2. Strengthen connections to key nodes */
   {
       int agent_id = processor->primary_agent;
       if (agent_id >= 0 && agent_id < kernel->agent_count) {
           Agent *agent = &kernel->agents[agent_id];
           
           /* Boost control node weights */
           for (i = 0; i < agent->control_count; i++) {
               int node_id = agent->control_nodes[i];
               if (node_id >= 0 && node_id < kernel->node_count) {
                   Node *node = &kernel->nodes[node_id];
                   int j;
                   
                   for (j = 0; j < node->connection_count; j++) {
                       if (node->weights[j] > 0) {
                           node->weights[j] *= 1.2; /* Strengthen positive connections */
                           if (node->weights[j] > 1.0) node->weights[j] = 1.0;
                       }
                   }
               }
           }
       }
   }
   
   /* 3. Temporarily increase priority */
   processor->priority += 0.2;
   if (processor->priority > 1.0) processor->priority = 1.0;
   
   /* 4. Reset entropy */
   processor->entropy = 0.1;
   
   printf("[Instance %d] Optimized dimension: %s\n", instance_id, processor->dimension_type);
}

void balance_dimensions(Kernel *kernel, MetaAgent *meta) {
   int i, j;
   
   if (!kernel || !meta) return;
   
   /* Adjust dimension balance factors */
   for (i = 0; i < kernel->dimension_count; i++) {
       for (j = i+1; j < kernel->dimension_count; j++) {
           /* Calculate indices for the balance matrix */
           int idx1 = i * kernel->max_dimensions + j;
           int idx2 = j * kernel->max_dimensions + i;
           
           /* Set to more balanced values */
           kernel->dimension_balance[idx1] = 0.5 + ((double)rand() / RAND_MAX) * 0.1 - 0.05; /* 0.45-0.55 */
           kernel->dimension_balance[idx2] = 0.5 + ((double)rand() / RAND_MAX) * 0.1 - 0.05; /* 0.45-0.55 */
       }
   }
   
   /* Adjust processor priorities to be more balanced */
   {
       double avg_priority = 0.0;
       
       /* Calculate average */
       for (i = 0; i < kernel->dimension_count; i++) {
           avg_priority += kernel->dimensions[i].priority;
       }
       avg_priority /= kernel->dimension_count;
       
       /* Adjust toward average */
       for (i = 0; i < kernel->dimension_count; i++) {
           kernel->dimensions[i].priority = 
               kernel->dimensions[i].priority * 0.7 + avg_priority * 0.3;
       }
   }
   
   /* Create connections between dimensions with low connectivity */
   for (i = 0; i < kernel->dimension_count; i++) {
       for (j = i+1; j < kernel->dimension_count; j++) {
           int agent_i = kernel->dimensions[i].primary_agent;
           int agent_j = kernel->dimensions[j].primary_agent;
           
           if (agent_i >= 0 && agent_i < kernel->agent_count && 
               agent_j >= 0 && agent_j < kernel->agent_count) {
               
               Agent *agent_i_ptr = &kernel->agents[agent_i];
               Agent *agent_j_ptr = &kernel->agents[agent_j];
               
               /* Connect a random control node from each agent */
               if (agent_i_ptr->control_count > 0 && agent_j_ptr->control_count > 0) {
                   int node_i = agent_i_ptr->control_nodes[rand() % agent_i_ptr->control_count];
                   int node_j = agent_j_ptr->control_nodes[rand() % agent_j_ptr->control_count];
                   
                   connect_nodes(kernel, node_i, node_j, 0.5 + ((double)rand() / RAND_MAX) * 0.3); /* 0.5-0.8 */
                   connect_nodes(kernel, node_j, node_i, 0.5 + ((double)rand() / RAND_MAX) * 0.3); /* 0.5-0.8 */
               }
           }
       }
   }
   
   printf("[Instance %d] Balanced dimension interactions\n", instance_id);
}

void boost_self_reference(Kernel *kernel, MetaAgent *meta) {
   int i, has_helix = 0;
   int helix_index = -1;
   
   if (!kernel || !meta) return;
   
   /* Check if Helix dimension exists */
   for (i = 0; i < kernel->dimension_count; i++) {
       if (strcmp(kernel->dimensions[i].dimension_type, "helix") == 0) {
           has_helix = 1;
           helix_index = i;
           break;
       }
   }
   
   /* If no Helix dimension and we have room, add one */
   if (!has_helix && kernel->dimension_count < kernel->max_dimensions) {
       add_dimension_processor(kernel, "meta_helix_processor", "helix", 0.4, 1.0);
       helix_index = kernel->dimension_count - 1;
       create_recursive_nodes(kernel); /* Create recursive node structures */
       
       printf("[Instance %d] Added new Helix dimension for self-reference\n", instance_id);
   }
   /* If Helix exists, strengthen it */
   else if (helix_index >= 0) {
       DimensionProcessor *helix = &kernel->dimensions[helix_index];
       int agent_id = helix->primary_agent;
       
       /* Increase priority and energy */
       helix->priority += 0.1;
       if (helix->priority > 1.0) helix->priority = 1.0;
       
       helix->energy = 0.9;
       
       /* Create additional self-connections in Helix agent nodes */
       if (agent_id >= 0 && agent_id < kernel->agent_count) {
           Agent *agent = &kernel->agents[agent_id];
           
           /* Add self-connections to rotation nodes */
           for (i = 0; i < agent->rotation_count; i++) {
               int node_id = agent->rotation_nodes[i];
               if (node_id >= 0 && node_id < kernel->node_count) {
                   Node *node = &kernel->nodes[node_id];
                   int has_self = 0;
                   int j;
                   
                   /* Check if self-connection exists */
                   for (j = 0; j < node->connection_count; j++) {
                       if (node->connections[j] == node_id) {
                           has_self = 1;
                           node->weights[j] += 0.1; /* Strengthen existing */
                           if (node->weights[j] > 1.0) node->weights[j] = 1.0;
                           break;
                       }
                   }
                   
                   /* Add self-connection if none exists */
                   if (!has_self && node->connection_count < MAX_CONNECTIONS) {
                       connect_nodes(kernel, node_id, node_id, 0.6);
                   }
                   
                   /* Increase rotation and momentum */
                   node->rotation += 0.1;
                   if (node->rotation > 1.0) node->rotation = 1.0;
                   
                   node->angular_momentum += 0.2;
                   if (node->angular_momentum > 1.0) node->angular_momentum = 1.0;
               }
           }
       }
       
       printf("[Instance %d] Boosted Helix dimension for self-reference\n", instance_id);
   }
}

void reduce_system_entropy(Kernel *kernel, MetaAgent *meta) {
   int i, j;
   
   if (!kernel || !meta) return;
   
   /* 1. Direct entropy reduction */
   kernel->entropy *= 0.8; /* Reduce by 20% */
   
   /* 2. Identify high-entropy nodes */
   for (i = 0; i < kernel->node_count; i++) {
       Node *node = &kernel->nodes[i];
       
       /* Target high-entropy nodes */
       if (node->entropy > 0.7) {
           /* Reduce node entropy */
           node->entropy *= 0.7;
           
           /* Strengthen stable connections */
           for (j = 0; j < node->connection_count; j++) {
               if (node->weights[j] > 0.6 || node->weights[j] < -0.6) {
                   /* Strengthen strong connections for stability */
                   node->weights[j] *= 1.1;
                   if (node->weights[j] > 1.0) node->weights[j] = 1.0;
                   if (node->weights[j] < -1.0) node->weights[j] = -1.0;
               }
               else if (fabs(node->weights[j]) < 0.2 && node->weights[j] != 0) {
                   /* Reduce very weak connections to reduce noise */
                   node->weights[j] *= 0.8;
               }
           }
       }
   }
   
   /* 3. Prioritize stability in dimension processors */
   for (i = 0; i < kernel->dimension_count; i++) {
       DimensionProcessor *processor = &kernel->dimensions[i];
       
       /* Reduce processor entropy */
       processor->entropy *= 0.8;
       
       /* Temporarily increase efficiency */
       processor->efficiency += 0.1;
       if (processor->efficiency > 1.0) processor->efficiency = 1.0;
   }
   
   /* 4. Boost Harmonia priority for integration */
   for (i = 0; i < kernel->dimension_count; i++) {
       if (strcmp(kernel->dimensions[i].dimension_type, "integration") == 0) {
           kernel->dimensions[i].priority += 0.15;
           if (kernel->dimensions[i].priority > 1.0) 
               kernel->dimensions[i].priority = 1.0;
           
           kernel->harmonia_priority = kernel->dimensions[i].priority;
           break;
       }
   }
   
   printf("[Instance %d] Reduced system entropy through multiple interventions\n", instance_id);
}

void reallocate_processor_priority(Kernel *kernel, MetaAgent *meta) {
   int i;
   double total_health = 0.0;
   double priority_adjustment = 0.1; /* How much to adjust by */
   
   if (!kernel || !meta) return;
   
   /* Calculate total health for normalization */
   for (i = 0; i < kernel->dimension_count; i++) {
       total_health += meta->dimension_health[i];
   }
   
   /* If total health is zero, avoid division by zero */
   if (total_health <= 0.01) {
       total_health = 0.01;
   }
   
   /* Allocate priorities inversely proportional to health */
   /* Dimensions with lower health get higher priority for improvement */
   for (i = 0; i < kernel->dimension_count; i++) {
       double health_factor = meta->dimension_health[i] / total_health;
       double inverse_factor = 1.0 - health_factor;
       
       /* Calculate new priority with limited change */
       double new_priority = kernel->dimensions[i].priority * (1.0 - priority_adjustment) +
                           inverse_factor * priority_adjustment;
       
       /* Apply with constraints */
       kernel->dimensions[i].priority = new_priority;
       if (kernel->dimensions[i].priority > 1.0) kernel->dimensions[i].priority = 1.0;
       if (kernel->dimensions[i].priority < 0.1) kernel->dimensions[i].priority = 0.1;
   }
   
   /* Update harmonia priority separately if it exists */
   for (i = 0; i < kernel->dimension_count; i++) {
       if (strcmp(kernel->dimensions[i].dimension_type, "integration") == 0) {
           kernel->harmonia_priority = kernel->dimensions[i].priority;
           break;
       }
   }
   
   printf("[Instance %d] Reallocated processor priorities based on health\n", instance_id);
}
