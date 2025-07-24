import numpy as np

def find_duplicates(ids: np.ndarray) -> np.ndarray:
  _, first_occurrence_indices = np.unique(ids, return_index=True)
  is_duplicate = np.ones(ids.shape, dtype=bool)
  is_duplicate[first_occurrence_indices] = False

  return is_duplicate
input_ids = np.array([1, 0, 0, 3, 0, 2, 4, 2, 2, 2, 2])
output_array = find_duplicates(input_ids)
print(output_array)