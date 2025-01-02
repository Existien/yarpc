/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/qt6/05_dicts.yml
 *   Template: qt6/types_header.j2
 */
#pragma once
#include "StructDict.hpp"
#include "SimonsDict.hpp"

namespace gen::dicts {

/**
* @brief Registers MetaTypes used by this interface.
*/
void registerMetaTypes();

bool operator!=(const QMap<QString, SimonsDict> &lhs, const QMap<QString, SimonsDict> &rhs);
bool operator!=(const QMap<QString, StructDict> &lhs, const QMap<QString, StructDict> &rhs);

}