# Error checking scheme
ERROR_CHECKING = "core.middleware.checks.crc.CRC"

# Error generator scheme
ERROR_GENERATOR = "core.device.datalink.error.error_generator"
ERROR_MAX_BITS = 2
ERROR_DISTRIBUTION = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1,
                      1, 1, 1, 1, 2, 2, 2, 3]

# Frame Settings
PACKET_SIZE = 32
