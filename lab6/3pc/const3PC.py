
# coordinator messages
VOTE_REQUEST = 'VOTE_REQUEST'
GLOBAL_COMMIT = 'GLOBAL_COMMIT'
GLOBAL_ABORT = 'GLOBAL_ABORT'
PREPARE_COMMIT = 'PREPARE_COMMIT'

# participant messages
VOTE_COMMIT = 'VOTE_COMMIT'
VOTE_ABORT = 'VOTE_ABORT'
NEED_DECISION = 'NEED_DECISION'
READY_COMMIT = 'READY_COMMIT'

# participant decisions
LOCAL_ABORT = 'LOCAL_ABORT'
LOCAL_SUCCESS = 'LOCAL_SUCCESS'

# fail-noisy crash timeout
TIMEOUT = 1
