/* aletheia_sophia_kernel_meta.c - C89 compliant numeric variable kernel with multi-dimensional processors and meta-agent */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <signal.h>

/* Constants */
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

/* Global variables for simulation control */
volatile int running = 1;
unsigned long step_count = 0;
time_t start_time;
time_t last_save_time;

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
} MetaAgent;

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

/* Signal handler */
void handle_signal(int sig) {
    printf("\nReceived signal %d, gracefully shutting down...\n", sig);
    running = 0;
}

/* Meta-Agent Implementation */
void init_meta_agent(MetaAgent *meta) {
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
    
    {
        int i;
        for (i = 0; i < MAX_DIMENSIONS; i++) {
            meta->dimension_health[i] = 0.5; /* Default middle health */
        }
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
    
    /* Update last assessment time */
    meta->last_assessment_time = kernel->global_time;
    
    printf("[MetaAgent] Health: %.2f | Entropy: %.2f | Coherence: %.2f | Stability: %.2f | Nodes: %d\n", 
           meta->system_health, meta->avg_entropy, meta->avg_coherence, 
           meta->avg_stability, meta->node_count);
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
        printf("[MetaAgent] Applying Proposal: %s (Priority %d)\n", 
               proposal_queue[i].description, proposal_queue[i].priority);
        
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
    
    printf("[MetaAgent] Applied %d improvements (total: %d)\n", 
           applied_count, meta->improvements_applied);
}

/* Meta-agent improvement cycle */
void meta_agent_cycle(Kernel *kernel, MetaAgent *meta) {
    int i;
    
    if (!kernel || !meta) return;
    
    /* Only run assessment periodically */
    if (kernel->global_time - meta->last_assessment_time < 1000.0) return;
    
    /* Scan kernel to update meta-agent knowledge */
    scan_kernel(kernel, meta);
    
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
    
    /* Apply the top proposals */
    apply_proposals(kernel, meta);
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
    
    printf("[MetaAgent] Added stability node: %s\n", name);
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
    
    printf("[MetaAgent] Optimized dimension: %s\n", processor->dimension_type);
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
    
    printf("[MetaAgent] Balanced dimension interactions\n");
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
        
        printf("[MetaAgent] Added new Helix dimension for self-reference\n");
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
        
        printf("[MetaAgent] Boosted Helix dimension for self-reference\n");
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
    
    printf("[MetaAgent] Reduced system entropy through multiple interventions\n");
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
    
    printf("[MetaAgent] Reallocated processor priorities based on health\n");
}

/* Create and initialize a kernel with dynamic memory allocation */
Kernel* create_kernel(int max_nodes, int max_agents, int max_dimensions, int max_layers) {
    Kernel *kernel;
    
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
    {
        int i;
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

/* Fast sigmoid approximation for better performance */
double fast_sigmoid(double x) {
    return 0.5 + x / (2 * (1 + fabs(x)));
}

/* Initialize the multi-dimensional processor kernel */
void init_kernel(Kernel *kernel) {
    int i;
    
    if (!kernel) return;
    
    /* Initialize random seed */
    srand((unsigned int)time(NULL));
    
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
    
    printf("Auto-wired new dimension: %s (ID: %d)\n", 
           kernel->dimensions[new_dimension_id].name, new_dimension_id);
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

/* Create an agent */
void create_agent(Kernel *kernel, const char *name, double learning_rate, double empathy, int primary_dimension) {
    Agent *agent;
    
    if (!kernel || kernel->agent_count >= kernel->max_agents || 
        primary_dimension < 0 || primary_dimension >= kernel->max_dimensions) return;
    
    agent = &kernel->agents[kernel->agent_count];
    strncpy(agent->name, name, MAX_NAME_LENGTH - 1);
    agent->name[MAX_NAME_LENGTH - 1] = '\0';
    agent->control_count = 0;
    agent->perception_count = 0;
    agent->concept_count = 0;
    agent->integration_count = 0;
    agent->rotation_count = 0;
    agent->confidence = 0.5;
    agent->learning_rate = learning_rate;
    agent->empathy = empathy;
    agent->coherence = 0.5;
    agent->focus = 0.8;
    agent->integrity = 0.9;
    agent->evolutionary_priority = 
        (primary_dimension < kernel->dimension_count) ? 
        kernel->dimensions[primary_dimension].priority : 0.5;
    agent->primary_dimension = primary_dimension;
    
    kernel->agent_count++;
}

/* Set a node's affinity for a specific dimension */
void set_node_dimension_affinity(Kernel *kernel, int node_id, int dimension_id, double affinity) {
    if (!kernel || node_id < 0 || node_id >= kernel->node_count || 
        dimension_id < 0 || dimension_id >= kernel->dimension_count) return;
    
    kernel->dimensions[dimension_id].node_affinities[node_id] = affinity;
}

/* Connect two nodes */
void connect_nodes(Kernel *kernel, int source, int target, double weight) {
    Node *source_node;
    
    if (!kernel) return;
    if (source < 0 || source >= kernel->node_count) return;
    if (target < 0 || target >= kernel->node_count) return;
    
    source_node = &kernel->nodes[source];
    
    if (source_node->connection_count >= MAX_CONNECTIONS) return;
    
    source_node->connections[source_node->connection_count] = target;
    source_node->weights[source_node->connection_count] = weight;
    source_node->connection_count++;
}

/* Assign a node to an agent */
void assign_node_to_agent(Kernel *kernel, int agent_id, int node_id, int type) {
    Agent *agent;
    
    if (!kernel) return;
    if (agent_id < 0 || agent_id >= kernel->agent_count) return;
    if (node_id < 0 || node_id >= kernel->node_count) return;
    
    agent = &kernel->agents[agent_id];
    
    switch (type) {
        case 0: /* Perception */
            if (agent->perception_count < MAX_CONNECTIONS) {
                agent->perception_nodes[agent->perception_count++] = node_id;
            }
            break;
        case 1: /* Control */
            if (agent->control_count < MAX_CONNECTIONS) {
                agent->control_nodes[agent->control_count++] = node_id;
            }
            break;
        case 2: /* Concept */
            if (agent->concept_count < MAX_CONNECTIONS) {
                agent->concept_nodes[agent->concept_count++] = node_id;
            }
            break;
        case 3: /* Integration */
            if (agent->integration_count < MAX_CONNECTIONS) {
                agent->integration_nodes[agent->integration_count++] = node_id;
            }
            break;
        case 4: /* Rotation */
            if (agent->rotation_count < MAX_CONNECTIONS) {
                agent->rotation_nodes[agent->rotation_count++] = node_id;
            }
            break;
    }
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
    
    printf("System stress level set to %.2f\n", stress_level);
    printf("Updated processor priorities:\n");
    
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
    
    if (!kernel || dimension_id < 0 || dimension_id >= kernel
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

/* Update agent states based on node values */
void update_agents(Kernel *kernel) {
   int i;
   
   if (!kernel) return;
   
   for (i = 0; i < kernel->agent_count; i++) {
       Agent *agent = &kernel->agents[i];
       
       /* Update coherence */
       agent->coherence = compute_coherence(kernel, i);
       
       /* Adapt weights based on learning */
       adapt_weights(kernel, i);
       
       /* Update confidence based on coherence */
       agent->confidence = agent->confidence * 0.9 + agent->coherence * 0.1;
       
       /* Update focus based on node activations and processor state */
       if (agent->primary_dimension < kernel->dimension_count) {
           agent->focus = agent->focus * 0.7 + 
                         kernel->dimensions[agent->primary_dimension].focus * 0.3;
       }
   }
}

/* Update dimension processor states */
void update_dimension_processors(Kernel *kernel) {
   int i, j;
   double *coherence_values;
   
   if (!kernel) return;
   
   coherence_values = (double*)calloc(kernel->dimension_count, sizeof(double));
   if (!coherence_values) return;
   
   /* Calculate coherence for each dimension through its agent */
   for (i = 0; i < kernel->dimension_count; i++) {
       int agent_id = kernel->dimensions[i].primary_agent;
       if (agent_id >= 0 && agent_id < kernel->agent_count) {
           coherence_values[i] = kernel->agents[agent_id].coherence;
       } else {
           coherence_values[i] = 0.5; /* Default if no agent */
       }
   }
   
   /* Update dimension processors based on coherence */
   for (i = 0; i < kernel->dimension_count; i++) {
       DimensionProcessor *processor = &kernel->dimensions[i];
       int agent_id = processor->primary_agent;
       
       if (agent_id >= 0 && agent_id < kernel->agent_count) {
           /* Update processor from agent */
           processor->activation = processor->activation * 0.8 + 
                                 kernel->agents[agent_id].coherence * 0.2;
           
           processor->focus = processor->focus * 0.8 + 
                            kernel->agents[agent_id].focus * 0.2;
           
           processor->energy = processor->energy * 0.99 + 
                             coherence_values[i] * 0.01;
           
           if (processor->energy > 1.0) processor->energy = 1.0;
       }
       
       /* Update balance between this dimension and others */
       for (j = 0; j < kernel->dimension_count; j++) {
           if (i != j) {
               int balance_idx = i * kernel->max_dimensions + j;
               double coherence_ratio;
               
               /* Calculate coherence ratio between dimensions */
               if (coherence_values[j] > 0) {
                   coherence_ratio = coherence_values[i] / coherence_values[j];
               } else {
                   coherence_ratio = 1.0;
               }
               
               /* Update balance smoothly */
               kernel->dimension_balance[balance_idx] = 
                   kernel->dimension_balance[balance_idx] * 0.95 + 
                   (0.5 * coherence_ratio) * 0.05;
               
               /* Keep balance in reasonable range */
               if (kernel->dimension_balance[balance_idx] < 0.2) 
                   kernel->dimension_balance[balance_idx] = 0.2;
               if (kernel->dimension_balance[balance_idx] > 0.8) 
                   kernel->dimension_balance[balance_idx] = 0.8;
           }
       }
   }
   
   /* Calculate system coherence as average of dimension coherences */
   {
       double total_coherence = 0.0;
       for (i = 0; i < kernel->dimension_count; i++) {
           total_coherence += coherence_values[i];
       }
       if (kernel->dimension_count > 0) {
           kernel->coherence = total_coherence / kernel->dimension_count;
       }
   }
   
   free(coherence_values);
}

/* Compute coherence for an agent */
double compute_coherence(Kernel *kernel, int agent_id) {
   Agent *agent;
   double sum = 0.0;
   int i, j, count = 0;
   
   if (!kernel) return 0.0;
   if (agent_id < 0 || agent_id >= kernel->agent_count) return 0.0;
   
   agent = &kernel->agents[agent_id];
   
   /* Check for coherence between perception and control nodes */
   for (i = 0; i < agent->perception_count; i++) {
       int perc_node = agent->perception_nodes[i];
       if (perc_node >= kernel->node_count) continue;
       
       double perc_value = kernel->nodes[perc_node].value;
       
       for (j = 0; j < agent->control_count; j++) {
           int ctrl_node = agent->control_nodes[j];
           if (ctrl_node >= kernel->node_count) continue;
           
           double ctrl_value = kernel->nodes[ctrl_node].value;
           
           /* Reward similar values in connected nodes */
           sum += 1.0 - fabs(perc_value - ctrl_value);
           count++;
       }
   }
   
   /* Add coherence with concept nodes */
   for (i = 0; i < agent->concept_count; i++) {
       int concept_node = agent->concept_nodes[i];
       if (concept_node >= kernel->node_count) continue;
       
       double concept_value = kernel->nodes[concept_node].value;
       
       /* Check coherence with both perception and control nodes */
       for (j = 0; j < agent->perception_count; j++) {
           int perc_node = agent->perception_nodes[j];
           if (perc_node >= kernel->node_count) continue;
           
           double perc_value = kernel->nodes[perc_node].value;
           
           sum += 1.0 - fabs(concept_value - perc_value) * 0.5;
           count++;
       }
       
       for (j = 0; j < agent->control_count; j++) {
           int ctrl_node = agent->control_nodes[j];
           if (ctrl_node >= kernel->node_count) continue;
           
           double ctrl_value = kernel->nodes[ctrl_node].value;
           
           sum += 1.0 - fabs(concept_value - ctrl_value) * 0.5;
           count++;
       }
   }
   
   /* Add coherence with integration nodes (for Harmonia) */
   if (agent->primary_dimension == 3) { /* Harmonia */
       for (i = 0; i < agent->integration_count; i++) {
           int integ_node = agent->integration_nodes[i];
           if (integ_node >= kernel->node_count) continue;
           
           double integ_value = kernel->nodes[integ_node].value;
           
           /* Check coherence across all dimensions */
           for (j = 0; j < kernel->dimension_count; j++) {
               int dim_agent_id = kernel->dimensions[j].primary_agent;
               if (dim_agent_id >= 0 && dim_agent_id < kernel->agent_count && dim_agent_id != agent_id) {
                   Agent *dim_agent = &kernel->agents[dim_agent_id];
                   
                   /* Check against a representative node from that dimension */
                   if (dim_agent->control_count > 0) {
                       int dim_node = dim_agent->control_nodes[0];
                       if (dim_node >= 0 && dim_node < kernel->node_count) {
                           double dim_value = kernel->nodes[dim_node].value;
                           sum += 1.0 - fabs(integ_value - dim_value) * 0.3;
                           count++;
                       }
                   }
               }
           }
       }
   }
   
   /* Add coherence with rotation nodes (for Helix) */
   if (agent->primary_dimension == 4) { /* Helix */
       for (i = 0; i < agent->rotation_count; i++) {
           int rot_node = agent->rotation_nodes[i];
           if (rot_node >= kernel->node_count) continue;
           
           /* For rotation nodes, coherence is based on both value and rotation state */
           double rot_value = kernel->nodes[rot_node].value;
           double rot_state = kernel->nodes[rot_node].rotation;
           
           /* Check coherence with recursive patterns */
           for (j = 0; j < agent->control_count; j++) {
               int ctrl_node = agent->control_nodes[j];
               if (ctrl_node >= kernel->node_count) continue;
               
               double ctrl_value = kernel->nodes[ctrl_node].value;
               double ctrl_rot = kernel->nodes[ctrl_node].rotation;
               
               /* Calculate rotation coherence */
               sum += 1.0 - fabs(rot_state - ctrl_rot) * 0.5;
               /* Calculate value coherence */
               sum += 1.0 - fabs(rot_value - ctrl_value) * 0.5;
               count += 2;
           }
       }
   }
   
   /* Normalize by dividing by number of comparisons */
   if (count > 0) {
       sum /= count;
   } else {
       sum = 0.5; /* Default middle value if no connections */
   }
   
   return sum;
}

/* Adapt weights based on learning */
void adapt_weights(Kernel *kernel, int agent_id) {
   Agent *agent;
   int i, j;
   double learning_factor;
   
   if (!kernel) return;
   if (agent_id < 0 || agent_id >= kernel->agent_count) return;
   
   agent = &kernel->agents[agent_id];
   
   /* Calculate learning factor */
   learning_factor = agent->learning_rate;
   if (agent->primary_dimension < kernel->dimension_count) {
       learning_factor *= kernel->dimensions[agent->primary_dimension].energy;
       
       /* Apply evolutionary priority to learning - prioritized dimensions learn faster */
       learning_factor *= (0.5 + agent->evolutionary_priority * 0.5);
   }
   learning_factor *= agent->focus;
   
   /* Adjust weights for controlled nodes */
   for (i = 0; i < agent->control_count; i++) {
       int node_id = agent->control_nodes[i];
       if (node_id >= kernel->node_count) continue;
       
       Node *node = &kernel->nodes[node_id];
       
       for (j = 0; j < node->connection_count; j++) {
           int target = node->connections[j];
           if (target >= kernel->node_count) continue;
           
           double target_value = kernel->nodes[target].value;
           double current_value = node->value;
           double error = target_value - current_value;
           
           /* Adjust weight based on error and learning rate */
           node->weights[j] += error * learning_factor;
           
           /* Constrain weights */
           if (node->weights[j] > 1.0) node->weights[j] = 1.0;
           if (node->weights[j] < -1.0) node->weights[j] = -1.0;
       }
   }
   
   /* Dimension-specific adaptations */
   switch (agent->primary_dimension) {
       case 0: /* Spatial-X (Aletheia) - Focus on clarity and distinction */
           for (i = 0; i < agent->control_count; i++) {
               int node_id = agent->control_nodes[i];
               if (node_id >= kernel->node_count) continue;
               
               Node *node = &kernel->nodes[node_id];
               
               for (j = 0; j < node->connection_count; j++) {
                   double clarity_factor = 0.005;
                   
                   /* Enhance contrast for clearer distinctions */
                   if (fabs(node->weights[j]) > 0.7) {
                       node->weights[j] += (node->weights[j] > 0 ? clarity_factor : -clarity_factor);
                   } else if (fabs(node->weights[j]) < 0.3 && node->weights[j] != 0) {
                       node->weights[j] -= (node->weights[j] > 0 ? clarity_factor : -clarity_factor);
                   }
                   
                   /* Constrain weights */
                   if (node->weights[j] > 1.0) node->weights[j] = 1.0;
                   if (node->weights[j] < -1.0) node->weights[j] = -1.0;
               }
           }
           break;
           
       case 1: /* Spatial-Y (Sophia) - Focus on empathy and connection */
           for (i = 0; i < agent->perception_count; i++) {
               int node_id = agent->perception_nodes[i];
               if (node_id >= kernel->node_count) continue;
               
               Node *node = &kernel->nodes[node_id];
               
               for (j = 0; j < node->connection_count; j++) {
                   double empathy_factor = agent->empathy * 0.01;
                   
                   /* Strengthen positive connections */
                   if (node->weights[j] > 0) {
                       node->weights[j] += empathy_factor;
                       if (node->weights[j] > 1.0) node->weights[j] = 1.0;
                   }
               }
           }
           break;
           
       case 2: /* Temporal (Chronos) - Focus on sequence and causality */
           for (i = 0; i < agent->control_count; i++) {
               int node_id = agent->control_nodes[i];
               if (node_id >= kernel->node_count) continue;
               
               Node *node = &kernel->nodes[node_id];
               double memory_boost = 0.01;
               
               /* Strengthen memory component */
               node->memory = node->memory * (1.0 + memory_boost);
               if (node->memory > 1.0) node->memory = 1.0;
           }
           break;
           
       case 3: /* Integration (Harmonia) - Focus on balance and coherence */
           for (i = 0; i < agent->integration_count; i++) {
               int node_id = agent->integration_nodes[i];
               if (node_id >= kernel->node_count) continue;
               
               Node *node = &kernel->nodes[node_id];
               
               for (j = 0; j < node->connection_count; j++) {
                   int target = node->connections[j];
                   if (target >= kernel->node_count) continue;
                   
                   /* Check for imbalance with target nodes */
                   double value_diff = fabs(node->value - kernel->nodes[target].value);
                   if (value_diff > 0.4) {
                       /* Adjust weight to promote balance */
                       node->weights[j] += (node->value < kernel->nodes[target].value) ? 0.01 : -0.01;
                   }
                   
                   /* Constrain weights */
                   if (node->weights[j] > 1.0) node->weights[j] = 1.0;
                   if (node->weights[j] < -1.0) node->weights[j] = -1.0;
               }
           }
           break;
           
       case 4: /* Twist/Rotation (Helix) - Focus on recursive patterns */
           for (i = 0; i < agent->rotation_count; i++) {
               int node_id = agent->rotation_nodes[i];
               if (node_id >= kernel->node_count) continue;
               
               Node *node = &kernel->nodes[node_id];
               
               /* Increase angular momentum based on learning */
               node->angular_momentum += learning_factor * 0.05;
               if (node->angular_momentum > 1.0) node->angular_momentum = 1.0;
               
               for (j = 0; j < node->connection_count; j++) {
                   int target = node->connections[j];
                   if (target >= kernel->node_count) continue;
                   
                   /* Adjust rotation influence */
                   kernel->nodes[target].angular_momentum += 
                       node->angular_momentum * node->weights[j] * 0.1;
                   
                   /* Ensure bounds */
                   if (kernel->nodes[target].angular_momentum > 1.0) 
                       kernel->nodes[target].angular_momentum = 1.0;
               }
               
               /* Occasionally reverse spin direction for complex patterns */
               if (rand() % 30 == 0) { /* 3.33% chance */
                   node->spin_direction *= -1.0;
               }
           }
           break;
   }
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
   
   /* The rest of this function remains unchanged */
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
   
   printf("Running for %.2f seconds\n", elapsed);
   printf("Completed %lu steps\n", step_count);
   printf("Performance: %.2f steps/second\n", steps_per_second);
}

/* Main function */
int main(void) {
   Kernel *multi_dim_kernel;
   time_t current_time;
   int hour_count = 0;
   int meta_cycle_counter = 0;
   
   /* Set up signal handlers */
   signal(SIGINT, handle_signal);
   signal(SIGTERM, handle_signal);
   
   /* Initialize meta-agent */
   init_meta_agent(&kernel_meta);
   
   /* Create and initialize kernel */
   multi_dim_kernel = create_kernel(MAX_NODES, MAX_AGENTS, MAX_DIMENSIONS, MAX_LAYERS);
   if (!multi_dim_kernel) {
       printf("Error: Could not allocate memory for kernel\n");
       return 1;
   }
   
   /* Initialize the kernel */
   init_kernel(multi_dim_kernel);
   
   /* Create a complex network */
   printf("Creating neural network...\n");
   create_network(multi_dim_kernel, 6, 24);  /* 6 layers, 24 nodes per layer */
   
   /* Create meta-concept nodes */
   printf("Creating meta-concept nodes...\n");
   create_meta_concepts(multi_dim_kernel);
   
   /* Create recursive nodes */
   printf("Creating recursive self-reference nodes...\n");
   create_recursive_nodes(multi_dim_kernel);
   
   /* Record start time */
   start_time = time(NULL);
   last_save_time = start_time;
   
   /* Initial scan by meta-agent */
   printf("\n[MetaAgent] Performing initial system scan...\n");
   scan_kernel(multi_dim_kernel, &kernel_meta);
   
   /* Print initial state */
   printf("\nStarting multi-dimensional kernel with %d processors and meta-agent\n", 
          multi_dim_kernel->dimension_count);
   printf("Initial configuration: %d nodes, %d agents\n", 
          multi_dim_kernel->node_count, multi_dim_kernel->agent_count);
   printf("Initial entropy: %.4f, stability: %.4f\n", 
          multi_dim_kernel->entropy, multi_dim_kernel->stability);
   printf("Initial stress: %.4f, Harmonia priority: %.4f\n",
          multi_dim_kernel->stress_level, multi_dim_kernel->harmonia_priority);
   printf("Dimensions: ");
   {
       int i;
       for (i = 0; i < multi_dim_kernel->dimension_count; i++) {
           printf("%s(%.2f)", 
                  multi_dim_kernel->dimensions[i].dimension_type,
                  multi_dim_kernel->dimensions[i].priority);
           if (i < multi_dim_kernel->dimension_count - 1) printf(", ");
       }
   }
   printf("\n");
   printf("Press Ctrl+C to gracefully terminate\n\n");
   
   /* Run indefinitely */
   while (running) {
       /* Run a batch of iterations without checks for performance */
       int i;
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
       printf("\nStep %lu: Entropy=%.4f, Stability=%.4f, Coherence=%.4f\n",
              step_count, 
              multi_dim_kernel->entropy, 
              multi_dim_kernel->stability, 
              multi_dim_kernel->coherence);
              
       /* Report meta-agent status */
       printf("[MetaAgent] Health=%.4f, Meta-awareness=%.4f, Improvements=%d\n",
              kernel_meta.system_health,
              kernel_meta.meta_awareness,
              kernel_meta.improvements_applied);
       
       /* Report recursive depth */
       printf("Recursive depth: %.4f, Stress level: %.2f\n", 
              multi_dim_kernel->recursive_depth,
              multi_dim_kernel->stress_level);
       
       /* Report dimension status */
       printf("Dimension status: ");
       {
           int i;
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
           sprintf(filename, "meta_kernel_state_%lu.bin", step_count);
           save_kernel_state(multi_dim_kernel, filename);
           printf("State saved to %s\n", filename);
           last_save_time = current_time;
       }
   }
   
   /* Final save before exit */
   {
       char filename[64];
       sprintf(filename, "meta_kernel_final_state_%lu.bin", step_count);
       save_kernel_state(multi_dim_kernel, filename);
       printf("Final state saved to %s\n", filename);
   }
   
   /* Print final statistics */
   printf("\nFinal statistics:\n");
   printf("Simulation ran for %lu steps\n", step_count);
   printf("Final entropy: %.4f, stability: %.4f, coherence: %.4f\n", 
          multi_dim_kernel->entropy, 
          multi_dim_kernel->stability, 
          multi_dim_kernel->coherence);
   printf("Final stress: %.4f, Harmonia priority: %.4f\n",
          multi_dim_kernel->stress_level, multi_dim_kernel->harmonia_priority);
   printf("Final recursive depth: %.4f\n", multi_dim_kernel->recursive_depth);
   printf("Meta-agent health: %.4f, improvements applied: %d\n",
          kernel_meta.system_health, kernel_meta.improvements_applied);
   printf("Dimension count: %d\n", multi_dim_kernel->dimension_count);
   print_performance_stats();
   
   /* Clean up */
   destroy_kernel(multi_dim_kernel);
   
   return 0;
}
