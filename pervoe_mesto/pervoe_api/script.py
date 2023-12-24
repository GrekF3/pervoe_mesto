import re

file_names = [
    "0000s-0000s-0000-pervoemesto-2k-67.3_250x250_c90.jpeg",
    "0000s-0000s-0001-pervoemesto-2k-66.7_250x250_c90.jpeg",
    "0000s-0000s-0002-pervoemesto-2k-66.6_250x250_c90.jpeg",
    "0000s-0000s-0003-pervoemesto-2k-65.8(1)_250x250_c90.jpeg",
    "0000s-0000s-0004-pervoemesto-2k-65.8_250x250_c90.jpeg",
    "0000s-0000s-0005-pervoemesto-2k-64.9_250x250_c90.jpeg",
    "0000s-0000s-0006-pervoemesto-2k-63.1_250x250_c90.jpeg",
    "0000s-0000s-0007-pervoemesto-2k-62.8_250x250_c90.jpeg",
    "0000s-0000s-0008-pervoemesto-2k-62.3_250x250_c90.jpeg",
    "0000s-0000s-0009-pervoemesto-2k-62.4_250x250_c90.jpeg",
    "0000s-0000s-0010-pervoemesto-2k-61.7_250x250_c90.jpeg",
    "0000s-0000s-0011-pervoemesto-2k-61.6_250x250_c90.jpeg",
    "0000s-0000s-0012-pervoemesto-2k-61.3_250x250_c90.jpeg",
    "0000s-0000s-0013-pervoemesto-2k-61.0_250x250_c90.jpeg",
    "0000s-0000s-0014-pervoemesto-2k-60.8(2)_250x250_c90.jpeg",
    "0000s-0000s-0015-pervoemesto-2k-60.8(1)_250x250_c90.jpeg",
    "0000s-0000s-0016-pervoemesto-2k-60.8_250x250_c90.jpeg",
    "0000s-0000s-0017-pervoemesto-2k-60.3(1)_250x250_c90.jpeg",
    "0000s-0000s-0018-pervoemesto-2k-60.3_250x250_c90.jpeg",
    "0000s-0000s-0019-pervoemesto-2k-60.1_250x250_c90.jpeg",
    "0000s-0000s-0020-pervoemesto-2k-60.0_250x250_c90.jpeg",
    "0000s-0000s-0021-pervoemesto-2k-59.9_250x250_c90.jpeg",
    "0000s-0000s-0022-pervoemesto-2k-59.5_250x250_c90.jpeg",
    "0000s-0000s-0023-pervoemesto-2k-58.8_250x250_c90.jpeg",
    "0000s-0000s-0024-pervoemesto-2k-58.4_250x250_c90.jpeg",
    "0000s-0000s-0025-pervoemesto-2k-48.4_250x250_c90.jpeg",
    "0000s-0000s-0026-pervoemesto-2k-47.5_250x250_c90.jpeg",
    "0000s-0000s-0027-pervoemesto-2k-47.2_250x250_c90.jpeg",
    "0000s-0000s-0028-pervoemesto-2k-46.6_250x250_c90.jpeg",
    "0000s-0000s-0029-pervoemesto-2k-43.6_250x250_c90.jpeg",
    "0000s-0000s-0030-pervoemesto-2k-42.7_250x250_c90.jpeg"
    
]

print(len(file_names))

pattern = r'(\d+\.\d+)'

for file_name in file_names:
    match = re.search(pattern, file_name)
    if match:
        size = match.group(1)
        print(size)