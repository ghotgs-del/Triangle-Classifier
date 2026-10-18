| Test | Copilot-suggested | Kept / editied / rejected | Why |

| test|right|triangle | Yes | Editied | I made sure it used math.isclose() instead of == because it would be unreliable for floating-point claculations. |

| test_is_valid_triangle | Yes | Kept| I checked the code and it was perfect. The test covers valid triangles, zero and negative sides, and invalid triangle boundaries |

| test_classify_triangle | Yes | Edited | I made sure the invlaid triangles return "Invalid" and not a long sentence saying the triangle was invalid. |

| test_,near_right_triangle_with floats | Yes | Kept | The test uses 5, 5, and 5 * math.sqrt(2) and expects "Right Isocseles". |


## Acceptance Criteria

1. **Buildability:** When any side is zero or negative or the sum of two sides is less than or equal to the third side, then the program will return "Invalid" without crashing.

2. **Shape identification:** For valid side lenghts, the program will return the correct triangle classification: "Equilateral", "Isosceles", or "Scalene".

3. **Reinforced corners:** When the sides form a right triangle, the program adds the classification with "Right" so the studio can identify pieces that need reinforced corners.


## Running the Tests

Run all the tests from the project folder using

python3 -m pytest -v

The tests should check triangle validity, triangle classifications, right triangles, and the stained-glass customer requirements.
